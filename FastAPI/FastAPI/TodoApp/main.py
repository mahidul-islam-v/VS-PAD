from typing import Annotated
from sqlalchemy.orm import Session
import models
from models import Todos
from fastapi import FastAPI, Depends, HTTPException
from database import engine, SessionLocal

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/")
async def read_all(db: db_dependency):
   return db.query(Todos).all()

@app.get("/todo/{todo_id}")
async def get_todo_by_id(db: db_dependency, todo_id: int):
   todo_res = db.query(Todos).filter(Todos.id == todo_id).first()

   if todo_res is not None:
       return todo_res
   
   raise HTTPException(status_code = 404, detail='Todo id not found in db')