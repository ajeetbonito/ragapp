from fastapi import APIRouter
from app.services.query_service import query_rag_model

router = APIRouter()

@router.get("/corpus")
async def corpus_builder(query: str):
    response = query_rag_model(query)
    return {"response": response}