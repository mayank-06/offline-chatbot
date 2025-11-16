from rag_chain import build_or_load_vectorstore

if __name__ == "__main__":
    vs = build_or_load_vectorstore()
    print("✅ Vectorstore ready with", vs._collection.count(), "chunks.")