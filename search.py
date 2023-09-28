from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback

def run_query(knowledge_base, question):
    docs = knowledge_base.similarity_search(question)
    chain = load_qa_chain(ChatOpenAI(), "stuff")
    with get_openai_callback() as callback:
        response = chain.run(input_documents=docs, question=question)
        cost = callback.total_cost
        return (response, cost)