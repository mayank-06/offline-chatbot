# ===============================
# utils/db_utils.py
# ===============================

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
import os
from pathlib import Path


def create_vector_db(file_path: str):
    """Create a FAISS index from a FAQ text file."""
    print("📂 Loading file:", file_path)
    loader = TextLoader(file_path)
    documents = loader.load()
    print(f"✅ Loaded {len(documents)} document(s).")

    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    docs = splitter.split_documents(documents)
    print(f"✅ Split into {len(docs)} chunks.")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.from_documents(docs, embeddings)
    db.save_local("faiss_index")
    print("🎉 FAISS index saved successfully at ./faiss_index/")


def load_vector_db():
    """Load an existing FAISS index."""
    if not os.path.exists("faiss_index"):
        raise FileNotFoundError("❌ FAISS index missing. Please upload FAQ file first.")
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return FAISS.load_local(
        "faiss_index", embeddings, allow_dangerous_deserialization=True
    )


# ------------------------------------------------------------
# Run this file directly to build the FAISS index manually
# ------------------------------------------------------------
if __name__ == "__main__":
    print("⚙️ Building FAISS index from data/faqs.txt ...")
    file_path = Path("data/faqs.txt")
    if not file_path.exists():
        print("❌ ERROR: data/faqs.txt not found! Please make sure the file exists.")
    else:
        create_vector_db(str(file_path))
        print("✅ Done! You can now run: streamlit run app.py")