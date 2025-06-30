
from langchain_core.tools.retriever import create_retriever_tool
from langchain_core.prompts import PromptTemplate

from common.rag.retriever import get_retriever

def get_retriever_tool():
  return create_retriever_tool(
    get_retriever(),
    "pdf_retriever",
    """
      Search and return information about SPRI AI Brief PDF file.
      It contains useful information on recent AI trends.
      The document is published on Dec 2023.
    """,
    document_prompt=PromptTemplate.from_template(
        "<document><context>{page_content}</context><metadata><source>{source}</source><page>{page}</page></metadata></document>"
    ),
)




