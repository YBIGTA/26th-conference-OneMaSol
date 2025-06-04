# """ from fastapi import APIRouter, WebSocket, Depends
# from typing import List
# from app.services.agent_service import AgentService, AuthService
# from app.schemas.agent import ChatMessage, ChatHistory

# router = APIRouter(prefix="/agent", tags=["AI Agent"])
# agent_service = AgentService()
# auth_service = AuthService()

# # 1) 실시간 챗 (WebSocket) => 웹소켓은 안쓸듯?
# #@router.websocket("/ws")
# #async def agent_ws(ws: WebSocket):
# #    await agent_service.handle_ws(ws)  # 토큰 확인은 내부에서

# # 2) 이전 대화 목록
# @router.get("/messages", response_model=List[ChatMessage])
# async def list_messages(limit: int = 50, current_user=Depends(auth_service.get_current_user)):
#     return await agent_service.list_messages(current_user.id, limit)

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