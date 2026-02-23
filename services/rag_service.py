from services.retrieval_service import retrieve_documents
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_question(question: str):
    docs = retrieve_documents(question)

    context = "\n\n".join([doc.content for doc in docs])

    prompt = f"""
You are a precise AI assistant.
Only answer using the provided context.
If not found, say you don't know.

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