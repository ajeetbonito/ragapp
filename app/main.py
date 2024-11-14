from fastapi import FastAPI
from app.routers import indexation, query, corpus
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.include_router(query.router)
app.include_router(corpus.router)
app.include_router(indexation.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the RAG App"}