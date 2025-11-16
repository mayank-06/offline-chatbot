import os
from typing import List
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import CSVLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from llm_local import get_local_llm

EMB_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
CHROMA_DIR = "chroma"

# ------------------------------------------------------------
# Load and split docs
# ------------------------------------------------------------
def _load_docs() -> List:
    docs = []
    if os.path.exists("data/faqs.csv"):
        docs += CSVLoader("data/faqs.csv").load()
    if os.path.exists("docs/policy.md"):
        docs += TextLoader("docs/policy.md", encoding="utf-8").load()
    if not docs:
        print("❌ No documents found.")
        return []
    splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=80)
    split_docs = splitter.split_documents(docs)
    print(f"✅ Loaded {len(docs)} files → {len(split_docs)} chunks.")
    return split_docs

# ------------------------------------------------------------
# Vector store
# ------------------------------------------------------------
def build_or_load_vectorstore():
    embeddings = HuggingFaceEmbeddings(model_name=EMB_MODEL)
    if os.path.exists(CHROMA_DIR) and os.listdir(CHROMA_DIR):
        print("✅ Loading existing Chroma store ...")
        return Chroma(persist_directory=CHROMA_DIR, embedding_function=embeddings)
    print("🔄 Creating new Chroma store ...")
    docs = _load_docs()
    if not docs:
        return None
    vs = Chroma.from_documents(docs, embedding=embeddings, persist_directory=CHROMA_DIR)
    vs.persist()
    print("✅ Vectorstore ready.")
    return vs

# ------------------------------------------------------------
# Retriever (simple & version-safe)
# ------------------------------------------------------------
def get_retriever():
    vs = build_or_load_vectorstore()
    if vs is None:
        return None
    return vs.as_retriever(search_kwargs={"k": 3})

# ------------------------------------------------------------
# QA Chain
# ------------------------------------------------------------
def get_qa_chain():
    llm = get_local_llm()
    retriever = get_retriever()
    if retriever is None:
        print("⚠ Retriever not ready.")
        return None

    template = """You are a helpful customer-support assistant.
Use ONLY the context below.  If the answer isn't in the context,
say you don't know and suggest contacting support.

Question: {question}
Context:
{context}

Answer:"""
    prompt = PromptTemplate.from_template(template)

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True,
    )
    return qa_chain