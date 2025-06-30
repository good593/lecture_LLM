from src.states import State

async def len_str(state:State) -> State:
    input = state["input"]
    result = len(input)
    return {
        "node_ouput": result,
        "is_stop":False
    }

async def add_one(state:State) -> State:
    input = state["node_ouput"]
    is_stop = state["is_stop"]

    result = input + 1
    if result > 10:
        is_stop = True

    return {
        **state, # state에 저장된 데이터를 다음 Node 전달
        "node_ouput": result,
        "is_stop": is_stop
    }

async def add_two(state:State) -> State:
    input = state["node_ouput"]
    result = input + 2
    return {
        **state, # state에 저장된 데이터를 다음 Node 전달
        "node_ouput": result
    }