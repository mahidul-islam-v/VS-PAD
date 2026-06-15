from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
async def first_api():
   return {'message': 'Hello Mahi'}