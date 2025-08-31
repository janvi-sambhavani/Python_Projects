from sqlmodel import SQLMODEL, Field
from typing import optional
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException

# Define the Item model
class Item(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    price: float
    is_offer: bool = False

# SQLite setup
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

# Create database and tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Dependency for DB session
def get_session():
    with Session(engine) as session:
        yield session

# FastAPI app setup with lifespan
app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    create_db_and_tables()
    yield
    # Shutdown

app.router.lifespan_context = lifespan

# POST endpoint to create items
@app.post("/items/")
def create_item(item: Item, session: Session = Depends(get_session)):
    session.add(item)
    session.commit()
    session.refresh(item)
    return item
