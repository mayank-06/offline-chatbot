# main.py

from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline
from chains.retrieval_chain import get_retrieval_chain

def answer_customer_query(query):
    generator = pipeline(
        "text2text-generation",
        model="google/flan-t5-base",
        max_length=256,
        temperature=0.2
    )

    llm = HuggingFacePipeline(pipeline=generator)

    chain = get_retrieval_chain(llm)

    result = chain(query)

    answer = result["result"]
    refs = [doc.page_content for doc in result["source_documents"]]

    return answer, refs