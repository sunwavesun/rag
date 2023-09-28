from PyPDF2 import PdfReader
from splitter import chunk_text
from embed import embed_text
from timer import timer

@timer
def process_pdf(path, chunk_size=256, chunk_overlap=30):
    text = pdf_to_text(path)
    chunked_text = chunk_text(text, chunk_size, chunk_overlap)
    vector = embed_text(chunked_text)
    return vector

def pdf_to_text(path):
    pdf_reader = PdfReader(path)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text