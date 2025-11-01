from datetime import datetime, timedelta, date
from typing import Optional, List, Literal

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, Field
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy import create_engine, String, Integer, ForeignKey, Date, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session

DATABASE_URL = "sqlite:///./erp.db"
JWT_SECRET = "CHANGE_ME_SUPER_SECRET"
JWT_ALGO = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24  # 1 day

engine = create_engine(DATABASE_URL, echo=False)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    role: Mapped[str] = mapped_column(String(20), index=True)  # 'admin' | 'teacher' | 'student'
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    tasks_assigned: Mapped[List["Task"]] = relationship(
        back_populates="student", foreign_keys="Task.student_id"
    )
    tasks_created: Mapped[List["Task"]] = relationship(
        back_populates="teacher", foreign_keys="Task.teacher_id"
    )

class Task(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    description: Mapped[str] = mapped_column(String(500))
    status: Mapped[str] = mapped_column(String(20), default="todo")  # todo | in_progress | done
    due_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)

    student_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    teacher_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    student: Mapped[User] = relationship(back_populates="tasks_assigned", foreign_keys=[student_id])
    teacher: Mapped[User] = relationship(back_populates="tasks_created", foreign_keys=[teacher_id])

Base.metadata.create_all(engine)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, password_hash: str) -> bool:
    return pwd_context.verify(plain_password, password_hash)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGO)

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6, max_length=128)

class UserOut(BaseModel):
    id: int
    username: str
    role: Literal["admin", "teacher", "student"]

    class Config:
        from_attributes = True

class TaskCreate(BaseModel):
    title: str
    description: str
    student_id: int
    due_date: Optional[date] = None

class TaskOut(BaseModel):
    id: int
    title: str
    description: str
    status: Literal["todo", "in_progress", "done"]
    due_date: Optional[date]
    student_id: int
    teacher_id: int
    created_at: datetime

    class Config:
        from_attributes = True

class TaskStatusUpdate(BaseModel):
    status: Literal["todo", "in_progress", "done"]

def get_db():
    with Session(engine) as session:
        yield session

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGO])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise credentials_exception
    return user


def require_role(*allowed_roles: str):
    def role_dep(current_user: User = Depends(get_current_user)) -> User:
        if current_user.role not in allowed_roles:
            raise HTTPException(status_code=403, detail="Not enough permissions")
        return current_user
    return role_dep
   
app = FastAPI(title="Mini ERP API", version="1.0.0")

@app.get("/")
def root():
    return {"message": "Welcome to Mini ERP API"}

class AdminBootstrap(BaseModel):
    username: str
    password: str

@app.post("/setup/create-admin", response_model=UserOut)
def create_admin(payload: AdminBootstrap, db: Session = Depends(get_db)):
    existing_admin = db.query(User).filter(User.role == "admin").first()
    if existing_admin:
        raise HTTPException(status_code=400, detail="Admin already exists")

    if db.query(User).filter(User.username == payload.username).first():
        raise HTTPException(status_code=400, detail="Username already taken")

    user = User(username=payload.username, password_hash=hash_password(payload.password), role="admin")
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.post("/auth/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    token = create_access_token({"sub": user.username, "role": user.role})
    return Token(access_token=token)

@app.post("/auth/register-teacher", response_model=UserOut)
def register_teacher(payload: UserCreate, db: Session = Depends(get_db), current_user: User = Depends(require_role("admin"))):
    if db.query(User).filter(User.username == payload.username).first():
        raise HTTPException(status_code=400, detail="Username already taken")
    user = User(username=payload.username, password_hash=hash_password(payload.password), role="teacher")
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.post("/auth/register-student", response_model=UserOut)
def register_student(payload: UserCreate, db: Session = Depends(get_db), current_user: User = Depends(require_role("admin"))):
    if db.query(User).filter(User.username == payload.username).first():
        raise HTTPException(status_code=400, detail="Username already taken")
    user = User(username=payload.username, password_hash=hash_password(payload.password), role="student")
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.post("/tasks", response_model=TaskOut)
def create_task(payload: TaskCreate, db: Session = Depends(get_db), teacher: User = Depends(require_role("teacher"))):
    student = db.query(User).filter(User.id == payload.student_id, User.role == "student").first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    task = Task(
        title=payload.title,
        description=payload.description,
        student_id=student.id,
        teacher_id=teacher.id,
        due_date=payload.due_date,
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

@app.get("/tasks", response_model=List[TaskOut])
def list_tasks(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.role == "student":
        return db.query(Task).filter(Task.student_id == current_user.id).order_by(Task.created_at.desc()).all()
    elif current_user.role == "teacher":
        return db.query(Task).filter(Task.teacher_id == current_user.id).order_by(Task.created_at.desc()).all()
    else:  # admin
        return db.query(Task).order_by(Task.created_at.desc()).all()

@app.patch("/tasks/{task_id}/status", response_model=TaskOut)
def update_status(task_id: int, payload: TaskStatusUpdate, db: Session = Depends(get_db), student: User = Depends(require_role("student"))):
    task = db.query(Task).filter(Task.id == task_id, Task.student_id == student.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found or not yours")
    task.status = payload.status
    db.commit()
    db.refresh(task)
    return task
   
class CountsOut(BaseModel):
    users: int
    students: int
    teachers: int
    tasks: int

@app.get("/stats/counts", response_model=CountsOut)
def counts(db: Session = Depends(get_db), _: User = Depends(get_current_user)):
    users = db.query(func.count(User.id)).scalar() or 0
    students = db.query(func.count(User.id)).filter(User.role == "student").scalar() or 0
    teachers = db.query(func.count(User.id)).filter(User.role == "teacher").scalar() or 0
    tasks = db.query(func.count(Task.id)).scalar() or 0
    return CountsOut(users=users, students=students, teachers=teachers, tasks=tasks)
