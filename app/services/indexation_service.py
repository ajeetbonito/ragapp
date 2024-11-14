from app.models import RAGModel
from pathlib import Path
import os

rag_model = RAGModel()

def index_docs():
    folder_path = Path(os.getenv("CORPUS_FOLDER"))
    result = rag_model.index_documents(folder_path)
    return "indexation completed"