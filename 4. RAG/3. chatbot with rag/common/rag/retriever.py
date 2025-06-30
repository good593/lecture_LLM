
from langchain_community.vectorstores import FAISS

from .embedding import get_embedding_of_openai
from .loader import get_docs_from_pdf

def get_retriever():
  db = FAISS.from_documents(
    documents=get_docs_from_pdf(), embedding=get_embedding_of_openai())
  
  return db.as_retriever()


