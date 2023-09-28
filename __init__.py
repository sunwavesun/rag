from dotenv import load_dotenv
from pdf import process_pdf

load_dotenv()

pdf = "pdfs/dsm5.pdf"
print(f"Creating a knowledge base for: {pdf}\n")
knowledge_base = process_pdf(pdf)