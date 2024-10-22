from fastapi import FastAPI
from app.routers import index, query

app = FastAPI()

# Include routers for different functionalities
app.include_router(query.router)
app.include_router(index.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the RAG App"}