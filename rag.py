# rag.py
import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from embeddings import generate_embedding
from openai import OpenAI

load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL"))
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def retrieve_documents(query, top_k=3):
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


def ask_question(question):
    docs = retrieve_documents(question)

    context = "\n\n".join([doc.content for doc in docs])

    prompt = f"""
You are an AI assistant. Use the provided context to answer the question.

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    answer = ask_question("Explain this project.")
    print(answer)