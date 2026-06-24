from fastapi import FastAPI

app = FastAPI()

class Book:
   def __init__(self, id, title, author, description, rating) -> None:
      self.id = id
      self.title = title
      self.author = author
      self.description = description
      self.rating = rating
      

Books: list = [22,22]

@app.get("/books")
async def first_api():
   return Books