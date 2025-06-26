# 🧠 FastAPI Embedding Service

A simple FastAPI microservice that generates vector embeddings from text using the `sentence-transformers` library (`all-MiniLM-L6-v2`).

---

## 🚀 Features

- Accepts a list of texts via POST request
- Returns dense vector embeddings (384-dim)
- Useful for powering product recommendation, search, or similarity systems
- Easily integrates with Qdrant, Pinecone, or other vector databases

---

## 📦 Requirements

- Python 3.8+
- pip

---

## 📁 Installation

```bash
# Clone the repo
git clone https://github.com/your-username/fastapi-embed-service.git
cd fastapi-embed-service

# Create virtual environment
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
