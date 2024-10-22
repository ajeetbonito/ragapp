from app.models import RAGModel

rag_model = RAGModel()

def query_rag_model(query: str):
    results = rag_model.search(query)
    if results:
        # Get the first result and pass it to the LLaMA model for further processing
        page_base64 = results[0].base64
        response = rag_model.get_llama_response(query, page_base64)
        return response
    return "No results found."