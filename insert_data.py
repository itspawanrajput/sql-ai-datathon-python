# insert_data.py
import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from embeddings import generate_embedding

load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL"))

def insert_document(title, content):
    embedding = generate_embedding(content)

    with engine.begin() as conn:
        conn.execute(
            text("""
                INSERT INTO documents (title, content, embedding)
                VALUES (:title, :content, :embedding)
            """),
            {
                "title": title,
                "content": content,
                "embedding": embedding
            }
        )

if __name__ == "__main__":
    insert_document(
        "SQL AI Datathon",
        "This project demonstrates vector search using PostgreSQL and OpenAI embeddings."
    )
    print("Inserted successfully")