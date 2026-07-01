from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel, Field
from datetime import date

app = FastAPI()

class Book:
   def __init__(self, id: int, title: str, author: str, description: str, rating: float, published_date: int) -> None:
      self.id = id
      self.title = title
      self.author = author
      self.description = description
      self.rating = rating
      self.puplished_date = published_date

class BookRequest(BaseModel):
   id: Optional[int] = Field(description="ID is not needed", default=None)
   title: str = Field(min_length=3, max_length=40)
   author: str = Field(min_length=3, max_length=40)
   description: str = Field(min_length=3, max_length=200)
   rating: float = Field(ge=0, le=5)
   published_date: int = Field(le=date.today().year)

   model_config = {
      "json_schema_extra": {
         "example":{
            "id": 0,
            "title": "Title One",
            "author": "Author One",
            "description": "Subject",
            "rating": 5,
            "published": 2012,
         }
      }
   }

Books: list = [
   Book(1, "Computer Science Pro", "faculty cse", "All knowledge of CSE", 5, 2001),
   Book(2, "Computer Science Basic", "faculty cse", "Basic knowledge of CSE", 3, 2017),
   Book(3, "Quantum Computing", "faculty cse", "Quantum computer knowledge", 5, 2010),
   Book(4, "Differential Calculus", "faculty mathematics", "Numbers and numbers", 4, 1998),
   Book(5, "Structured Programming Language", "faculty cse", "C and C++", 4.5, 2019),
]

@app.get("/books")
async def first_api():
   return Books

@app.get("/books/{book_id}")
async def get_book_by_id(book_id: int = Path(ge=0)):
   for book in Books:
      if book.id == book_id:
         return book
   
@app.get("/books/")
async def get_book_by_rating(book_rating: int):
   books_to_return = []
   for book in Books:
      if book.rating == book_rating:
         books_to_return.append(book)
   return books_to_return

# Post
@app.post("/books/create-book")
async def post_books(book_request: BookRequest):
   new_book = Book(**book_request.model_dump())
   new_book.id = 1 + (Books[-1].id if len(Books)>0 else 0)
   Books.append(new_book)
   return new_book

# PUT
@app.put("/books/update_book")
async def update_book(new_book: BookRequest):
   for i in range(len(Books)):
      if Books[i].id == new_book.id:
         Books[i] = new_book
         return "Books Updated"
   return "Can not find ID"

# DELETE
@app.delete("/books/{book_id}")
async def delete_book(book_id: int = Path(ge=1)):
   for i in range(len(Books)):
      if Books[i].id == book_id:
         Books.pop(i)
         break