import __init__
from pdf import process_pdf
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback

pdf = "pdfs/dsm5.pdf"
print(f"Creating a knowledge base for: {pdf}\n")
knowledge_base = process_pdf(pdf)
model_name = input("Provide a model name (defaults to `gpt-3.5-turbo`): ")
if model_name is not True:
    model_name = "gpt-3.5-turbo"
print(f"Using model: {model_name}\n")

while True:
    query = input("Ask a question: ")

    if query:
        docs = knowledge_base.similarity_search(query)
        llm = ChatOpenAI(model_name=model_name)
        # TODO: Difference between `chain_type`
        chain = load_qa_chain(llm, "stuff")
        with get_openai_callback() as cost:
            response = chain.run(input_documents=docs, question=query)
            print(f"Answer: {response}")
            print(f"Cost: {cost}\n")
    else:
        print("Not a valid question!\n")
            