
# 🧠 MindDoc-RAG

**MindDoc-RAG** is an AI-powered document assistant that uses **Retrieval-Augmented Generation (RAG)** to intelligently answer questions from PDF documents. This project integrates the **GROQ API**, **LangChain**, and **ChromaDB** for a fast, local, and flexible Q&A experience over documents.

---

## 🚀 Features

- ✅ Upload and process PDF documents
- 🤖 Ask questions and receive context-aware answers
- ⚡ Powered by GROQ LLMs for lightning-fast responses
- 🧩 Built with LangChain for modular orchestration
- 🗂️ Local vector storage with ChromaDB
- 🌐 Easy to deploy and use on any machine

---

## 🛠️ Tech Stack

- **Python**
- **GROQ API** (for LLM responses)
- **LangChain** (for building the RAG pipeline)
- **ChromaDB** (as vector store)
- **Streamlit** (optional UI for testing)

---

## 📂 Project Structure
MindDoc-RAG/
│
├── .env                      # Contains your GROQ_API_KEY (never push this to GitHub)
├── .gitignore                # To exclude .env, __pycache__, etc.
├── README.md                 # Project overview and instructions
├── requirements.txt          # All project dependencies
├── app.py                    # Main entry point or Streamlit app
│
├── chroma_store/             # ChromaDB database files (can be .gitignored)
│
├── vectorstore/             # Vector store or persisted DB (optional, can be merged with chroma_store)
│
├── modules/                  # Core logic separated by functionality
│   ├── llm.py                # Loads GROQ API, LangChain & builds RAG chain
│   ├── file_handler.py       # Loads and processes PDF files
│   ├── chroma_inspector.py   # Debugs or inspects ChromaDB content
│   └── chat.py               # Handles user queries and chat logic
│
└── myenv/                    # Local virtual environment (should be .gitignored)
