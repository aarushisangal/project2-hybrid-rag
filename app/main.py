from fastapi import FastAPI

from app.api.query import router as query_router


app = FastAPI(
    title="Project 2 - Hybrid RAG Sandbox",
    description="Document ingestion and hybrid retrieval pipeline",
    version="1.0.0"
)


app.include_router(query_router)


@app.get("/")
def root():

    return {
        "message": "Hybrid RAG Sandbox is running"
    }