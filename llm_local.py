from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from langchain_community.llms import HuggingFacePipeline

# Small, CPU-friendly local model
MODEL_NAME = "google/flan-t5-small"

_pipe = None

def get_local_llm():
    """Return a lightweight local HuggingFace text2text model wrapped for LangChain."""
    global _pipe
    if _pipe is None:
        print("🔄 Loading local model (FLAN-T5-small)...")
        tok = AutoTokenizer.from_pretrained(MODEL_NAME)
        mdl = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
        _pipe = pipeline(
            "text2text-generation",
            model=mdl,
            tokenizer=tok,
            max_new_tokens=256
        )
        print("✅ Model loaded successfully!")
    return HuggingFacePipeline(pipeline=_pipe)