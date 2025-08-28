
import streamlit as st
from langchain_community.vectorstores import Chroma

def inspect_chroma(vectorstore):
    """Enhanced ChromaDB Inspector with better error handling and display"""
    st.sidebar.markdown("### 🔍 ChromaDB Inspector")
    
    # Show basic info with more details
    try:
        collection = vectorstore._collection
        doc_count = collection.count()
        st.sidebar.success(f"✅ Documents stored: **{doc_count}**")

        
        
        # Display collection metadata
    except Exception as e:
         st.sidebar.error("⚠️ Could not fetch ChromaDB information")
         st.sidebar.exception(e)  # More detailed error than str(e)
    
    