# chains/retrieval_chain.py

from utils.db_utils import load_vector_db
from langchain.memory import ConversationBufferMemory
from langchain.chains.retrieval_qa.base import RetrievalQA

def get_retrieval_chain(llm):
    db = load_vector_db()

    retriever = db.as_retriever(search_kwargs={"k": 3})

    # Memory must store only ONE key → so we declare output_key="result"
    memory = ConversationBufferMemory(
        memory_key="history",
        return_messages=True,
        output_key="result"    # ⭐ THIS FIXES YOUR ERROR
    )

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        memory=memory,
        return_source_documents=True,
        output_key="result"    # ⭐ REQUIRED FOR MULTIPLE OUTPUTS
    )

    return chain