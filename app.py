from fastapi import FastAPI
from ingest import ingest_faq,ingest_pdf

app= FastAPI()
@app.get("/search")
def search(q:str):
    faq = open("data/faqs.txt").read()
    pdf = open("data/long_doc.txt").read()

    faq_chunks , faq_vecs = ingest_faq(faq)
    pdf_chunks, pdf_vecs = ingest_pdf(pdf)
    return {
        "query":q,
        "faq_chunks": len(faq_chunks),
        "pdf_chunks":len(pdf_chunks),
        "message":"Optimized chunking-better semantic converage"
    }