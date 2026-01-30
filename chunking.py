# short doc in if chunking applied so it complete change the meaning of the words . so all place in not same embadding are applyed
def chunk_faq(text):
    return [text.strip()]

def chunk_pdf(text,chunk_size=400,overlap=50):
    words= text.split()
    chunks =[]
    i =0
    while i<len(words):
        chunk = words[i:i+chunk_size]
        chunks.append(" ".join(chunk))
        i += chunk_size -overlap
    return chunks