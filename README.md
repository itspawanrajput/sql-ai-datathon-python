# 🚀 AI-Powered SQL RAG System (Open Hack Project)

[![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.131+-009688?logo=fastapi)](https://fastapi.tiangolo.com)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-412991?logo=openai)](https://platform.openai.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17_AWS_RDS-336791?logo=postgresql)](https://github.com/pgvector/pgvector)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

## 📌 Overview

This project demonstrates a **production-style Retrieval-Augmented Generation (RAG) system** built using:

- 🐘 **PostgreSQL** (AWS RDS)
- 🧠 **OpenAI Embeddings & LLM**
- 🔎 **pgvector** for semantic search
- ⚡ **FastAPI** for API layer
- 🧩 **Modular service architecture**

The system enables users to ask natural language questions and receive answers **grounded in stored database content** using vector similarity search.

---

## 🏗️ Architecture

```
User
  ↓
FastAPI (/ask endpoint)
  ↓
RAG Service
  ↓
Retrieval Service
  ↓
PostgreSQL (AWS RDS + pgvector)
  ↓
OpenAI Embeddings + Chat Model
```

---

## 🎯 Problem Statement

Traditional SQL search relies on:
- Exact matches
- `LIKE` queries
- Keyword search

This project enhances search capabilities using:
- **Vector embeddings**
- **Semantic similarity**
- **Context-aware AI responses**

It bridges structured databases with modern GenAI systems.

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Database | PostgreSQL 17 (AWS RDS) |
| Vector Search | pgvector |
| AI Embeddings | OpenAI `text-embedding-3-small` |
| LLM | OpenAI `gpt-4o-mini` |
| Backend | FastAPI |
| ORM | SQLAlchemy |
| Environment | Python (`uv` managed) |

---

## 📂 Project Structure

```
sql-ai-datathon-python/
│
├── db/
│   └── connection.py           # SQLAlchemy engine setup
│
├── services/
│   ├── embeddings_service.py   # OpenAI embedding generation
│   ├── retrieval_service.py    # pgvector cosine similarity search
│   └── rag_service.py          # RAG orchestration
│
├── missions/
│   └── mission1_embeddings/    # Mission 1: Embeddings & Vector Search
│
├── main.py                     # FastAPI server
├── app.py                      # CLI interactive Q&A loop
├── embeddings.py               # Standalone embedding utility
├── insert_data.py              # Insert documents into DB
├── search.py                   # Standalone vector search
├── rag.py                      # Standalone RAG pipeline
├── test_connection.py          # DB connectivity test
├── .env.example                # Environment variable template
├── requirements.txt            # pip dependencies
└── pyproject.toml              # uv project config
```

---

## 🔍 How It Works

### 1️⃣ Embedding Generation

Text content is converted into vector embeddings using OpenAI:

```python
generate_embedding(text)
```

Embeddings are stored in PostgreSQL using the `VECTOR(1536)` datatype.

### 2️⃣ Semantic Retrieval

When a user asks a question:
- The query is embedded
- Vector similarity search is performed using:

```sql
ORDER BY embedding <-> CAST(:query_embedding AS vector)
```

This retrieves the most semantically relevant documents.

### 3️⃣ Retrieval-Augmented Generation (RAG)

Retrieved content is injected into a structured prompt:

```
Context:
<retrieved documents>

Question:
<user question>
```

The LLM generates an answer **grounded strictly in the retrieved context**. Hallucination protection is enforced via prompt constraints.

---

## 🚀 Running the Project

### 1. Clone the Repository

```bash
git clone https://github.com/itspawanrajput/sql-ai-datathon-python.git
cd sql-ai-datathon-python
```

### 2. Install Dependencies

```bash
uv sync
# or with pip:
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
cp .env.example .env
```

Edit `.env`:

```env
OPENAI_API_KEY=your_key
DATABASE_URL=postgresql+psycopg2://user:password@host:5432/postgres
```

### 4. Enable pgvector in PostgreSQL

```sql
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS documents (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    embedding VECTOR(1536)
);
```

### 5. Run API Server

```bash
uv run uvicorn main:app --reload
```

Open: `http://127.0.0.1:8000/docs`

Test endpoint:

```
GET /ask?q=What does this project demonstrate?
```

---

## 📊 Example Output

```json
{
  "question": "What does this project demonstrate?",
  "answer": "This project demonstrates vector search using PostgreSQL and OpenAI embeddings."
}
```

---

## 🔐 Security Considerations

- SSL-enabled database connection
- Restricted RDS security group (IP-based access)
- No public exposure of secrets
- Environment variables for all configuration (`.env` excluded from git)

---

## 📈 Future Improvements (Open Hack Extensions)

- [ ] Document chunking for improved retrieval accuracy
- [ ] Batch ingestion pipeline
- [ ] IVFFLAT / HNSW vector indexing
- [ ] Authentication & API rate limiting
- [ ] Docker containerization
- [ ] EC2 deployment
- [ ] Frontend chat UI

---

## 🧠 Key Learnings

- Vector databases inside relational systems
- `pgvector` indexing strategies
- Prompt engineering for RAG systems
- AWS networking (VPC, security groups, SSL)
- Modular backend design
- Production-ready API patterns

---

## 💼 Why This Project Matters

This project demonstrates:
- **Cloud-native AI architecture**
- **SQL + AI integration**
- **Real-world RAG pipeline**
- **End-to-end system design**

It reflects practical implementation of modern GenAI systems used in startups and enterprise environments.

---

## 🏆 About the Challenge

Built for the **[Microsoft SQL AI Datathon](https://github.com/microsoft/sql-ai-datathon)** — a hands-on challenge to build AI-powered applications using SQL databases with vector search capabilities.

---

*Built with ❤️ for the Microsoft SQL AI Datathon*
