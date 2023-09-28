import __init__
from flask import Flask, jsonify, request
from pdf import process_pdf
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
from search import run_query

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    if not request.json or "question" not in request.json:
        return jsonify({"error": "Missing question in request body"}), 400
    
    question = request.json.get("question", "")
    response, cost = run_query(knowledge_base, question)

    return jsonify({
        "question": question,
        "response": response,
        "cost": cost,
    })

if __name__ == '__main__':
    pdf = "pdfs/dsm5.pdf"
    print(f"Creating a knowledge base for: {pdf}\n")
    knowledge_base = process_pdf(pdf)

    app.run()