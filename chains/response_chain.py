from langchain.prompts import PromptTemplate
from langchain.llms import HuggingFacePipeline
from transformers import pipeline
from langchain.chains import LLMChain

def get_response_chain():
    prompt_template = """
    You are a helpful and polite customer support assistant.
    Respond clearly and accurately to customer questions.

    Question: {question}
    """

    prompt = PromptTemplate(template=prompt_template, input_variables=["question"])
    generator = pipeline("text2text-generation", model="google/flan-t5-base")
    llm = HuggingFacePipeline(pipeline=generator)
    return LLMChain(prompt=prompt, llm=llm)