from app.dto.agent_dto import ChatRequest, ChatResponse
from typing import List

async def run_agent_chat(request: ChatRequest) -> ChatResponse:
    # LangGraph 실행 시뮬레이션
    task_id = "task-" + request.user_id[:6]
    used_agents: List[str] = ["TaskRouter", "RAGFeasibilityRouter", "RAGRetriever", "RAGQualityCritic"]

    response_text = f"'{request.message}'에 대한 응답입니다. (시뮬레이션)"

    result = {
        "answer": response_text,
        "task_id": task_id,
        "used_agents": used_agents,
        "final": True
    }

    return ChatResponse(**result)