from langchain_community.retrievers import BM25Retriever
from langchain.tools import Tool
from retriever import docs

bm25_retriever = BM25Retriever.from_documents(docs)

def extract_text(query: str) -> str:
    """"Retrieves detalied info about gala guest based on their name or relation."""
    results = bm25_retriever.invoke(query)
    if results:
        return "\n\n".join([doc.text for doc in results[:3]])
    else:
        return "No matching guest info ."

guest_info_tool=Tool(
    name="guest_info_retriever",
    func=extract_text,
    description="Retrieves detailed info about gala guest based on their name or relation. "
)

