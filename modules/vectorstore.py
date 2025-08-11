from langchain_community.vectorstores import Chroma  #To create and manage the vector database 
from langchain.document_loaders import PyPDFLoader  # To load PDF document
from langchain.document_loaders import Docx2txtLoader  # To load DOCX document
from langchain.embeddings import HuggingFaceEmbeddings  # To convert text into embeddings [numerical vector]
from langchain.text_splitter import RecursiveCharacterTextSplitter  #To split long text into smaller chunks
from modules.file_handler import save_uploaded_files  # custom function to save the uploaded file
import os

PERSIST_DIR = "./chroma_store"  #drfine the folder to store vector database


def load_vectorstore(uploaded_files):
    paths = save_uploaded_files(uploaded_files)
    
    docs = []
    for path in paths:
        if path.endswith('.pdf'):
            loader = PyPDFLoader(path)
        elif path.endswith('.docx'):
            loader = Docx2txtLoader(path)
        else:
            continue  # Skip unsupported file types
        docs.extend(loader.load())
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = splitter.split_documents(docs)
    
    embeddings = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
    
    if os.path.exists(PERSIST_DIR) and os.listdir(PERSIST_DIR):
        # Append to existing
        vectorstore = Chroma(persist_directory=PERSIST_DIR, embedding_function=embeddings)
        vectorstore.add_documents(texts)
        vectorstore.persist()
    else:
        # Create new
        vectorstore = Chroma.from_documents(
            documents=texts,
            embedding=embeddings,
            persist_directory=PERSIST_DIR
        )
        vectorstore.persist()
    

    return vectorstore
