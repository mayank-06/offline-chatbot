from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import HuggingFacePipeline
from transformers import pipeline
from utils.db_utils import load_vector_db

def get_memory_chain():
    db = load_vector_db()
    retriever = db.as_retriever(search_kwargs={"k": 3})
    generator = pipeline("text2text-generation", model="google/flan-t5-base", max_length=256)
    llm = HuggingFacePipeline(pipeline=generator)
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=retriever, memory=memory)
    return chain