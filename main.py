from fastapi import FastAPI, Request
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer

app = FastAPI()
model = SentenceTransformer("all-MiniLM-L6-v2")

class EmbedRequest(BaseModel):
    texts: list[str]

@app.post("/embed")
async def embed_text(req: EmbedRequest):
    try:
        vectors = model.encode(req.texts).tolist()
        return {"vectors": vectors}
    except Exception as e:
        return {"error": str(e)}

