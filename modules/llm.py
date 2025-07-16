import os
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq

load_dotenv()

def get_llm_chain(vectorstore):
    groq_api_key = os.getenv("GROQ_API_KEY")

    if not groq_api_key:
        raise ValueError("❌ GROQ_API_KEY is missing. Check your .env file.")

    llm = ChatGroq(
        api_key=groq_api_key,
        model_name="llama-3.1-8b-instant"
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(),
        return_source_documents=True
    )

    return qa_chain
