from fastapi import FastAPI

app = FastAPI()

books = [
    {"title": "Title One", "text": "Hello"},
    {"title": "Title Two", "text": "World"}
]

@app.get("/books")
async def first_api():
   return books

@app.get("/books/{book_title}")
async def second_api(book_title):
   for book in books:
      if book["title"].casefold() == book_title:
         return book