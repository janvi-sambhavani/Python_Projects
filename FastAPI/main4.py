from fastapi import FastAPI
from contextlib import asynccontextmanager
from typing import Optional, List
from sqlmodel import SQLModel, Field, Session, create_engine, select

# PostgreSQL connection URI (hide in .env in production)
postgres_uri = "postgresql://postgres.wgadcjwmtaaqlwcnmakd:6Vus3dH5LElqhQov@aws-0-ap-south-1.pooler.supabase.com:6543/postgres""

# Define SQLModel model
class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: float
    is_offer: bool = False

# Create engine
engine = create_engine(postgres_uri, echo=True)

# Create tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Lifespan for FastAPI app
@asynccontextmanager
def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

# Initialize app with lifespan
app = FastAPI(lifespan=lifespan)

# POST endpoint to create an item
@app.post("/items/")
def create_item(item: Item):
    with Session(engine) as session:
        session.add(item)
        session.commit()
        session.refresh(item)
        return item

# GET endpoint to read all items
@app.get("/items/", response_model=List[Item])
def read_items():
    with Session(engine) as session:
        items = session.exec(select(Item)).all()
        return items
