from langchain_core.documents import Document

from core.rag_engine import ask_question, build_rag_chain, format_docs, load_rag_chain
from core.vector_store import build_vector_store, get_retriever, load_vector_store


def test_vector_store_operations():
    transcript = "This is a test transcript for building the vector store. It contains multiple sentences for testing."
    vector_store = build_vector_store(transcript)
    assert vector_store is not None

    loaded_store = load_vector_store()
    assert loaded_store is not None

    retriever = get_retriever(loaded_store, k=2)
    assert retriever is not None

def test_format_docs():
    docs = [Document(page_content="Hello"), Document(page_content="World")]
    formatted = format_docs(docs)
    assert formatted == "Hello\n\nWorld"

def test_rag_chain_execution():
    transcript = "The team decided to launch the product in Q3. Action item: John will finalize the documentation by Friday."
    rag_chain = build_rag_chain(transcript)
    assert rag_chain is not None

    # Test asking question
    answer = ask_question(rag_chain, "When will the product launch?")
    assert isinstance(answer, str)
    assert len(answer) > 0

def test_load_rag_chain():
    rag_chain = load_rag_chain()
    assert rag_chain is not None
