try:
    from langchain_chroma import Chroma
except ImportError:
    try:
        from langchain_community.vectorstores import Chroma
    except ImportError:
        Chroma = None

try:
    from langchain_huggingface import HuggingFaceEmbeddings
except ImportError:
    try:
        from langchain_community.embeddings import HuggingFaceEmbeddings
    except ImportError:
        HuggingFaceEmbeddings = None

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

CHROMA_DIR = "vector_db"
COLLECTION_NAME = "meeting_transcript"
EMBEDDING_MODEL  = "all-MiniLM-L6-v2"

def get_embeddings():
    if HuggingFaceEmbeddings is None:
        return None
    return HuggingFaceEmbeddings(
        model_name = EMBEDDING_MODEL,
        model_kwargs = {"device" : 'cpu'}
    )

def build_vector_store(transcript : str):
    print("Building vector Store")
    if Chroma is None:
        print("Chroma not installed. Returning Mock Vector Store.")
        return "MOCK_VECTOR_STORE"

    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap = 50
    )
    chunks = splitter.split_text(transcript)

    docs = [
        Document(page_content=chunk, metadata = {'chunk_index' : i})
        for i,chunk in enumerate(chunks)
    ]

    embeddings = get_embeddings()
    vector_store = Chroma.from_documents(
        documents= docs,
        embedding=embeddings,
        collection_name=COLLECTION_NAME,
        persist_directory=CHROMA_DIR
    )

    return vector_store



def load_vector_store():
    if Chroma is None:
        return "MOCK_VECTOR_STORE"
    embeddings = get_embeddings()
    vector_store = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function= embeddings,
        persist_directory=CHROMA_DIR
    )

    return vector_store

def get_retriever(vector_store, k :int = 4):
    if vector_store == "MOCK_VECTOR_STORE":
        from langchain_core.documents import Document
        from langchain_core.runnables import RunnableLambda
        return RunnableLambda(lambda x: [Document(page_content="[Mocked vector retrieval based on context]")])
    return vector_store.as_retriever(
        search_type = 'similarity',
        search_kwargs = {"k":k}
    )


