from pydantic import BaseModel
from typing import Optional, List

class ChatRequest(BaseModel):
    user_id: str
    session_id: Optional[str]
    message: str

class ChatResponse(BaseModel):
    answer: str
    task_id: Optional[str]
    used_agents: List[str]
    final: bool

class ChatSessionSummary(BaseModel):
    session_id: str
    session_title: Optional[str]
    last_active_at: Optional[str]

class ChatLog(BaseModel):
    chat_id: str
    message: str
    role: str
    step_order: int
    created_at: str

class ChatSessionDetailResponse(BaseModel):
    session_id: str
    logs: List[ChatLog]

class ChatSessionTraceResponse(BaseModel):
    current_node: str
    search_retry_count: int
    used_agents: List[str]

class CalendarCreateRequest(BaseModel):
    user_id: str
    title: str
    start_at: str
    end_at: str
    location: Optional[str] = None
    description: Optional[str] = None

class CalendarUpdateRequest(BaseModel):
    title: Optional[str]
    start_at: Optional[str]
    end_at: Optional[str]
    location: Optional[str]
    description: Optional[str]

class TaskCreateRequest(BaseModel):
    user_id: str
    title: str
    description: Optional[str]

class TaskCreateResponse(BaseModel):
    task_id: str
    status: str

class AgentLogRequest(BaseModel):
    session_id: str
    task_id: Optional[str]
    agent_type: str
    input_text: str
    output_text: str
    status: str