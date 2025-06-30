
from langchain_core.prompts import PromptTemplate


def get_prompt_of_relevance():
    # 프롬프트 템플릿 정의
  return PromptTemplate(
      template="""You are a grader assessing relevance of a retrieved document to a user question. \n
      Here is the retrieved document: \n\n {context} \n\n
      Here is the user question: {question} \n
      If the document contains keyword(s) or semantic meaning related to the user question, grade it as relevant. \n
      Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question.""",
      input_variables=["context", "question"],
  )




