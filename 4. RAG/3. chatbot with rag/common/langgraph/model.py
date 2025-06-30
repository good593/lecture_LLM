
from typing import Literal
from langchain import hub
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import tools_condition

# 최신 모델이름 가져오기
MODEL_NAME = "gpt-4o-mini"


# 데이터 모델 정의
class grade(BaseModel):
    """A binary score for relevance checks"""

    binary_score: str = Field(
        description="Response 'yes' if the document is relevant to the question or 'no' if it is not."
    )

def get_model_of_relevance(model_name = "gpt-4o-mini"):
    model = ChatOpenAI(temperature=0, model=model_name, streaming=True)

    # 구조화된 출력을 위한 LLM 설정
    return model.with_structured_output(grade)


def get_model(model_name = "gpt-4o-mini"):
    return ChatOpenAI(temperature=0, model=model_name, streaming=True)

