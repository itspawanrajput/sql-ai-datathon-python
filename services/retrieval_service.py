from sqlalchemy import text
from db.connection import engine
from services.embeddings_service import generate_embedding

def retrieve_documents(query: str, top_k: int = 3):
    query_embedding = generate_embedding(query)

    with engine.connect() as conn:
        result = conn.execute(
            text("""
                SELECT title, content
                FROM documents
                ORDER BY embedding <-> CAST(:query_embedding AS vector)
                LIMIT :limit
            """),
            {"query_embedding": query_embedding, "limit": top_k}
        )

        return result.fetchall()