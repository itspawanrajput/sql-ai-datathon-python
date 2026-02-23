# search.py
import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from embeddings import generate_embedding

load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL"))

def search(query):
    query_embedding = generate_embedding(query)

    with engine.connect() as conn:
        result = conn.execute(
            text("""
                SELECT id, title, content
                FROM documents
                ORDER BY embedding <-> CAST(:query_embedding AS vector)
                LIMIT 3
            """),
            {"query_embedding": query_embedding}
        )

        return result.fetchall()


if __name__ == "__main__":
    results = search("What is this project about?")
    for row in results:
        print(row)