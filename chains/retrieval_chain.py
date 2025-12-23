# chains/retrieval_chain.py

from utils.db_utils import load_vector_db
from langchain_core.memory import ConversationBufferMemory
from langchain.chains import RetrievalQA


def get_retrieval_chain(llm):
    db = load_vector_db()

    retriever = db.as_retriever(search_kwargs={"k": 3})

    # Memory must store only ONE key → output_key must match chain output
    memory = ConversationBufferMemory(
        memory_key="history",
        return_messages=True,
        output_key="result"
    )

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        memory=memory,
        return_source_documents=True,
        output_key="result"
    )

    return chain
