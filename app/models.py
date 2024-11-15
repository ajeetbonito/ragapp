from byaldi import RAGMultiModalModel
from together import Together
from pathlib import Path
import os

class RAGModel:
    def __init__(self):
        self.model = RAGMultiModalModel.from_pretrained("vidore/colqwen2-v0.1")
        self.index_name = os.getenv("INDEX_NAME")
        self.client = Together(api_key= os.getenv("TOGETHER_API_KEY"))

    def index_documents(self, docs_folder: str):
        self.model.index(
            input_path=Path(docs_folder),
            index_name=self.index_name,
            store_collection_with_index=True,
            overwrite=True,
        )

    def search(self, query: str):
        results = self.model.search(query, k=1)
        return results

    def get_llama_response(self, query: str, image_base64: str):
        response = self.client.chat.completions.create(
            model="meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": query},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"}}
                    ]
                }
            ],
            max_tokens=300,
        )
        return response.choices[0].message.content
