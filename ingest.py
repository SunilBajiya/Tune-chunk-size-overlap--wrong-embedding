from sentence_transformers import SentenceTransformer 
from chunking import chunk_faq , chunk_pdf 

model = SentenceTransformer("all-MiniLM-L6-V2") 

def ingest_faq(text):
    chunks = chunk_faq(text) 
    return chunks, model.encode(chunks) 

def ingest_pdf(text):
    chunks = chunk_pdf(text)
    return chunks, model.encode(chunks) 