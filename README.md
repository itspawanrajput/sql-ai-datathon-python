# 🧠 SQL AI Datathon — Python RAG Solution

> My Python implementation for the **[Microsoft SQL AI Datathon](https://github.com/microsoft/sql-ai-datathon)** — building a full Retrieval-Augmented Generation (RAG) pipeline using **PostgreSQL + pgvector** and **OpenAI GPT-4o-mini**, exposed as a **FastAPI** service.

[![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.131+-009688?logo=fastapi)](https://fastapi.tiangolo.com)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-412991?logo=openai)](https://platform.openai.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-pgvector-336791?logo=postgresql)](https://github.com/pgvector/pgvector)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 📌 What This Project Does

This project answers natural language questions by:

1. **Generating embeddings** from text using `text-embedding-3-small`
2. **Storing them** in a PostgreSQL database with the `pgvector` extension
3. **Searching** the database using cosine similarity (`<->` operator)
4. **Answering** questions via GPT-4o-mini with the retrieved context (RAG pattern)

```
User Question
     │
     ▼
[Embedding Model] ──► Generate query vector
     │
     ▼
[PostgreSQL + pgvector] ──► Cosine similarity search → Top-K documents
     │
     ▼
[GPT-4o-mini] ──► RAG prompt → Natural language answer
```

---

## 🗂️ Project Structure

```
sql-ai-datathon-python/
│
├── app.py                  # CLI interactive Q&A loop
├── main.py                 # FastAPI web server entry point
├── embeddings.py           # Embedding generation (standalone)
├── insert_data.py          # Insert documents with embeddings into DB
├── search.py               # Vector similarity search (standalone)
├── rag.py                  # Full RAG pipeline (standalone)
├── test_connection.py      # Verify database connectivity
│
├── db/
│   └── connection.py       # SQLAlchemy engine setup
│
├── services/
│   ├── embeddings_service.py   # Embedding generation service
│   ├── retrieval_service.py    # Vector similarity retrieval
│   └── rag_service.py          # RAG orchestration (retrieve → prompt → answer)
│
├── missions/
│   └── mission1_embeddings/    # Mission 1: Embeddings & Vector Search
│
├── pyproject.toml          # Project metadata & dependencies (uv)
├── requirements.txt        # pip-compatible dependencies
├── .env.example            # Environment variable template
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.12+
- PostgreSQL with [`pgvector`](https://github.com/pgvector/pgvector) extension enabled
- An [OpenAI API key](https://platform.openai.com/api-keys)

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/sql-ai-datathon-python.git
cd sql-ai-datathon-python
```

### 2. Set Up Environment Variables

```bash
cp .env.example .env
```

Edit `.env` with your credentials:

```env
OPENAI_API_KEY=sk-proj-...
DATABASE_URL=postgresql+psycopg2://postgres:yourpassword@localhost:5432/yourdb
```

### 3. Install Dependencies

**Using pip:**
```bash
pip install -r requirements.txt
```

**Using uv (recommended):**
```bash
pip install uv
uv sync
```

### 4. Enable pgvector in PostgreSQL

Connect to your database and run:

```sql
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS documents (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    embedding VECTOR(1536)
);
```

### 5. Test the Database Connection

```bash
python test_connection.py
# Expected output: 1
```

---

## 🧪 Usage

### Insert a Document

```bash
python insert_data.py
```

This generates an embedding for the sample document and stores it in the database.

### Search with Vector Similarity

```bash
python search.py
```

Queries the database using cosine similarity and returns the top-3 most relevant documents.

### Run the RAG Pipeline (CLI)

```bash
python app.py
```

Interactive loop — ask any question, get an AI-powered answer grounded in your documents:

```
Ask: What is this project about?
Answer:
 This project demonstrates vector search using PostgreSQL and OpenAI embeddings...
```

### Run the FastAPI Server

```bash
uvicorn main:app --reload
```

Then visit: `http://localhost:8000/ask?q=What+is+this+project+about`

Example response:
```json
{
  "question": "What is this project about?",
  "answer": "This project demonstrates vector search using PostgreSQL and OpenAI embeddings."
}
```

API Docs available at: `http://localhost:8000/docs`

---

## ⚙️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.12 |
| AI / LLM | OpenAI GPT-4o-mini |
| Embeddings | OpenAI text-embedding-3-small (1536 dims) |
| Vector DB | PostgreSQL + pgvector |
| ORM | SQLAlchemy |
| API Server | FastAPI + Uvicorn |
| Env Management | python-dotenv |

---

## 🏆 About the Challenge

This is my solution for the **[Microsoft SQL AI Datathon](https://github.com/microsoft/sql-ai-datathon)** — a hands-on challenge to build AI-powered applications using SQL databases with vector search capabilities.

**Mission 1:** Generate embeddings with OpenAI and store them in PostgreSQL using pgvector, then implement cosine similarity search and a full RAG pipeline.

---

## 🔐 Security Note

Never commit your `.env` file. The `.gitignore` is configured to exclude it. Use `.env.example` as a template.

---

## 📄 License

This project is open source under the [MIT License](LICENSE).

---

*Built with ❤️ for the Microsoft SQL AI Datathon*
