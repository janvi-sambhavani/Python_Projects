from fastapi import FastAPI
from contextlib import asynccontextmanager
from typing import Optional, List
from sqlmodel import SQLModel, Field, Session, create_engine, select

postgres_uri = "postgresql://postgres.wgadcjwmtaaqlwcnmakd:6Vus3dH5LElqhQov@aws-0-ap-south-1.pooler.supabase.com:6543/postgres""

class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: float
    is_offer: bool = False

engine = create_engine(postgres_uri, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@asynccontextmanager
def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/items/")
def create_item(item: Item):
    with Session(engine) as session:
        session.add(item)
        session.commit()
        session.refresh(item)
        return item

@app.get("/items/", response_model=List[Item])
def read_items():
    with Session(engine) as session:
        items = session.exec(select(Item)).all()
        return items
