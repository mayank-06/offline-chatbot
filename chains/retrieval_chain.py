# chains/retrieval_chain.py

from utils.db_utils import load_vector_db
from langchain.chains import RetrievalQA


def get_retrieval_chain(llm):
    db = load_vector_db()

    retriever = db.as_retriever(search_kwargs={"k": 3})

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        return_source_documents=True
    )

    return chain
