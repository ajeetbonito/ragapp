from app.models import RAGModel
from pathlib import Path

rag_model = RAGModel()

def index_doc():
    folder_path = Path(CORPUS_FOLDER)
    result = rag_model.index_documents(folder_path)