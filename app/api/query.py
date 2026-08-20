from fastapi import APIRouter
from pydantic import BaseModel

from app.retrieval.retriever import Retriever


router = APIRouter()

retriever = Retriever(
    collection_name="test_documents"
)


class QueryRequest(BaseModel):
    query: str
    retrieve_k: int = 10
    final_k: int = 3


@router.post("/query")
def query_documents(request: QueryRequest):

    results = retriever.search(
        query=request.query,
        retrieve_k=request.retrieve_k,
        final_k=request.final_k
    )

    return {
        "query": request.query,
        "results": [
            {
                "text": document,
                "score": float(score)
            }
            for document, score in results
        ]
    }