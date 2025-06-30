from typing import Literal
from langchain_core.messages import HumanMessage

from common.langgraph.states import AgentState
from common.langgraph.model import get_model_of_relevance, get_model
from common.langgraph.prompt import get_prompt_of_relevance
from common.langgraph.tools import get_retriever_tool

async def grade_documents(state:AgentState) -> Literal["generate", "rewrite"]:
  # llm + tool 바인딩 체인 생성
  chain = get_prompt_of_relevance() | get_model_of_relevance()

  # 현재 상태에서 메시지 추출
  messages = state["messages"]

  # 관련성 평가 실행
  scored_result = chain.invoke({
          # 원래 질문 추출
          "question": messages[0].content, 
          # 검색된 문서 추출
          "context": messages[-1].content
      })

  # 관련성 여부에 따른 결정
  if scored_result.binary_score == "yes":
      print("==== [DECISION: DOCS RELEVANT] ====")
      return "generate"

  print("==== [DECISION: DOCS NOT RELEVANT] ====")
  print(scored_result.binary_score)
  return "rewrite"

async def agent(state:AgentState):
    # 현재 상태에서 메시지 추출
    messages = state["messages"]

    # LLM 모델 초기화
    model = get_model().bind_tools([get_retriever_tool()])

    # 에이전트 응답 생성
    response = model.invoke(messages)

    # 기존 리스트에 추가되므로 리스트 형태로 반환
    return {"messages": [response]}

async def rewrite(state:AgentState):
    print("==== [QUERY REWRITE] ====")
    # 현재 상태에서 메시지 추출
    messages = state["messages"]
    # 원래 질문 추출
    question = messages[0].content

    # 질문 개선을 위한 프롬프트 구성
    msg = [
        HumanMessage(
            content=f""" \n
                Look at the input and try to reason about the underlying semantic intent / meaning. \n
                Here is the initial question:
                \n ------- \n
                {question}
                \n ------- \n
                Formulate an improved question: """,
        )
    ]

    # LLM 모델로 질문 개선
    model = get_model()
    # Query-Transform 체인 실행
    response = model.invoke(msg)

    # 재작성된 질문 반환
    return {"messages": [response]}




