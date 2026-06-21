from fastapi import FastAPI, Body

app = FastAPI()

books: list = [
    {"title": "Title One", "author": "Author One", 'category': "science"},
    {"title": "Title Two", "author": "Author Two", 'category': "science"},
    {"title": "Title Three", "author": "Author Three", 'category': "history"},
    {"title": "Title Four", "author": "Author Four", 'category': "math"},
    {"title": "Title Five", "author": "Author Five", 'category': "math"},
    {"title": "Title six", "author": "Author Two", 'category': "math"}
]

@app.get("/books")
async def first_api():
   return books

@app.get("/books/{book_title}")
async def dynamic_api(book_title: str):
   for book in books:
      if book["title"].casefold() == book_title.casefold():
         return book
      
@app.get("/books/")
async def return_books_by_category(category: str):
   books_to_return = []
   for book in books:
      if book.get("category", "").casefold() == category.casefold():
         books_to_return.append(book)
   
   return books_to_return

@app.post("/books/create")
async def create_book(new_book=Body()):
   books.append(new_book)

@app.put("/books/update_book")
async def update_book(new_book=Body()):
   for book in books:
      if book.get("title", "").casefold() == new_book.get("title", "").casefold():
         book = new_book