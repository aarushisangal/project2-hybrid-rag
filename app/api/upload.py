from pathlib import Path
import shutil

from fastapi import APIRouter, UploadFile, File, Form, HTTPException

from app.parsers.pdf_parser import read_pdf
from app.parsers.docx_parser import read_docx
from app.chunking.pipeline import create_chunks
from app.embeddings.embedder import Embedder
from app.vectorstore.chroma_store import ChromaStore


router = APIRouter()


UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


embedder = Embedder()

vectorstore = ChromaStore(
    collection_name="test_documents"
)


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    method: str = Form("semantic")
):
    """
    Upload a PDF or DOCX document, parse it, chunk it,
    generate embeddings, and store the chunks in ChromaDB.
    """

    # 1. Validate chunking method
    allowed_methods = {
        "character",
        "structure",
        "semantic"
    }

    if method not in allowed_methods:
        raise HTTPException(
            status_code=400,
            detail=(
                f"Unsupported chunking method: {method}. "
                f"Choose from: {sorted(allowed_methods)}"
            )
        )

    # 2. Validate file type
    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No filename provided."
        )

    file_path = UPLOAD_DIR / file.filename
    extension = file_path.suffix.lower()

    if extension not in {".pdf", ".docx"}:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are currently supported."
        )

    try:

        # 3. Save uploaded file
        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # 4. Parse document
        if extension == ".pdf":
            text = read_pdf(file_path)

        elif extension == ".docx":
            text = read_docx(file_path)

        # 5. Validate extracted text
        if not text.strip():
            raise HTTPException(
                status_code=400,
                detail="No text could be extracted from the document."
            )

        # 6. Create chunks
        chunks = create_chunks(
            text=text,
            source=file.filename,
            method=method
        )

        if not chunks:
            raise HTTPException(
                status_code=400,
                detail="No chunks were created from the document."
            )

        # 7. Generate embeddings
        texts = [
            chunk.text
            for chunk in chunks
        ]

        embeddings = embedder.encode(texts)

        # 8. Store chunks + embeddings in ChromaDB
        vectorstore.add_chunks(
            chunks=chunks,
            embeddings=embeddings
        )

        # 9. Return information about the upload
        return {
            "message": "Document uploaded and indexed successfully.",
            "filename": file.filename,
            "chunking_method": method,
            "chunks_created": len(chunks),
            "collection": "test_documents"
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing document: {str(e)}"
        )