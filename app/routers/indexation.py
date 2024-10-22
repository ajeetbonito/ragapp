from fastapi import APIRouter
from app.services.indexation_service import index_doc

router = APIRouter()

@router.get("/index")
async def index_documents():
    response = index_docs()
    return {"response": response}