from fastapi import FastAPI
from services.rag_service import ask_question

app = FastAPI()

@app.get("/ask")
def ask(q: str):
    answer = ask_question(q)
    return {"question": q, "answer": answer}