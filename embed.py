from langchain.embeddings.openai import OpenAIEmbeddings
from langchain import FAISS

def embed_text(text, vector=FAISS, embedding=OpenAIEmbeddings):
     return vector.from_texts(text, embedding())