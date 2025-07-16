import tempfile  # used to create temporary files 
import streamlit as st  # Streamlit for web app
from PyPDF2 import PdfReader  # PyPDF2 library for reading PDF files
from docx import Document  # python-docx library for reading DOCX files

def upload_files():
    """Handle both PDF and DOCX file uploads"""
    with st.sidebar:
        st.header("Upload Documents")
        uploaded_files = st.file_uploader(
            "Choose files", 
            type=["pdf", "docx"], 
            accept_multiple_files=True
        )
        submit = st.button("Submit to Database")
    return uploaded_files, submit

def save_uploaded_files(uploaded_files):
    """Save uploaded files to temporary files and return their paths"""
    file_paths = []
    for file in uploaded_files:
        with tempfile.NamedTemporaryFile(delete=False, suffix=f'.{file.name.split(".")[-1]}') as tmp:
            tmp.write(file.read())
            file_paths.append(tmp.name)
    return file_paths

def extract_text_from_file(file_path):
    """Extract text from either PDF or DOCX files"""
    if file_path.endswith('.pdf'):
        reader = PdfReader(file_path)
        text = " ".join([page.extract_text() for page in reader.pages])
    elif file_path.endswith('.docx'):
        doc = Document(file_path)
        text = " ".join([paragraph.text for paragraph in doc.paragraphs])
    else:
        raise ValueError("Unsupported file format")
    return text