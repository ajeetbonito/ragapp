from fastapi import APIRouter
from app.services.query_service import query_rag_model

router = APIRouter()

@router.get("/query")
async def query_model(query: str):
    response = query_rag_model(query)
    return {"response": response}