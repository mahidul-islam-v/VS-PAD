from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

class Book:
   def __init__(self, id, title, author, description, rating) -> None:
      self.id = id
      self.title = title
      self.author = author
      self.description = description
      self.rating = rating

Books: list = [
   Book(1, "Computer Science Pro", "faculty cse", "All knowledge of CSE", 5),
   Book(2, "Computer Science Basic", "faculty cse", "Basic knowledge of CSE", 3),
   Book(3, "Quantum Computing", "faculty cse", "Quantum computer knowledge", 5),
   Book(4, "Differential Calculus", "faculty mathematics", "Numbers and numbers", 4),
   Book(5, "Structured Programming Language", "faculty cse", "C and C++", 4.5),
]

@app.get("/books")
async def first_api():
   return Books

@app.post("/create-book")
async def post_books(book_request=Body()):
   Books.append(book_request)

