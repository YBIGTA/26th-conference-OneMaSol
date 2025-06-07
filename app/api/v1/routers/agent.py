# """ from fastapi import APIRouter, WebSocket, Depends
# from typing import List
# from app.services.agent_service import AgentService, AuthService
# from app.schemas.agent import ChatMessage, ChatHistory

from fastapi import APIRouter, Depends, Path, Query
from typing import List
from app.dto.agent_dto import (
    ChatRequest, ChatResponse,
    TaskCreateRequest, TaskResponse,
    AgentLogRequest,
    SessionTraceResponse
)
from app.services.agent_service import AgentService, AuthService

router = APIRouter(prefix="/agent", tags=["AI Agent"])
agent_service = AgentService()
auth_service = AuthService()


# # 1) 실시간 챗 (WebSocket) => 웹소켓은 안쓸듯?
# #@router.websocket("/ws")
# #async def agent_ws(ws: WebSocket):
# #    await agent_service.handle_ws(ws)  # 토큰 확인은 내부에서

# 실시간 챗 응답
@router.post("/chat", response_model=ChatResponse)
async def agent_chat(request: ChatRequest):
    return await agent_service.process_chat(request)

# # 2) 이전 대화 목록
# @router.get("/messages", response_model=List[ChatMessage])
# async def list_messages(limit: int = 50, current_user=Depends(auth_service.get_current_user)):
#     return await agent_service.list_messages(current_user.id, limit)

# 세션 내 메시지 목록 조회
@router.get("/chat/sessions/{session_id}", response_model=List[ChatResponse])
async def get_session_messages(session_id: str):
    return await agent_service.get_messages_in_session(session_id)

# # 3) 챗으로 일정 CRUD
# #@router.post("/messages", response_model=ChatMessage)
# #async def send_message(
#     payload: ChatMessage,
#     current_user=Depends(auth_service.get_current_user)
# #):
#     """
#    "예) "5월 30일 14시에 회의 잡아줘" → calendar_service 연동
#     """
#     return await agent_service.process_message(current_user.id, payload)
#  """

# 일정 추가
@router.post("/calendar", response_model=dict)
async def add_calendar_event():
    return await agent_service.add_event()

# 일정 삭제
@router.delete("/calendar/{event_id}", response_model=dict)
async def delete_calendar_event(event_id: str = Path(...)):
    return await agent_service.delete_event(event_id)

# 일정 수정
@router.put("/calendar/{event_id}", response_model=dict)
async def update_calendar_event(event_id: str = Path(...)):
    return await agent_service.update_event(event_id)

# 태스크 생성
@router.post("/tasks", response_model=TaskResponse)
async def create_task(request: TaskCreateRequest):
    return await agent_service.create_task(request)

# 태스크 조회
@router.get("/tasks/{task_id}", response_model=TaskResponse)
async def get_task(task_id: str = Path(...)):
    return await agent_service.get_task(task_id)

# 에이전트 실행 로그 저장
@router.post("/logs")
async def save_agent_log(log: AgentLogRequest):
    return await agent_service.save_log(log)


# 유저 전체 세션 목록
@router.get("/chat/sessions", response_model=List[str])
async def get_all_sessions(user_id: str = Query(...)):
    return await agent_service.get_sessions_for_user(user_id)

# 세션 트레이스 (흐름 추적)
@router.get("/chat/sessions/{session_id}/trace", response_model=SessionTraceResponse)
async def get_session_trace(session_id: str):
    return await agent_service.get_trace_for_session(session_id)