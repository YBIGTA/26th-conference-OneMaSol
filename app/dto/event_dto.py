"""
캘린더 이벤트 DTO
----------------
Create · Update · Read(공개) 세 가지로 분리
"""

from typing import Optional
import datetime as dt
from datetime import datetime
from pydantic import BaseModel, Field, validator
import uuid

class _EventBase(BaseModel):
    class Config:
        """
        공통 필드에 대한 설정
        - datetime 포맷: yyyy-MM-dd HH:mm:ss
        """
        json_encoders = {
            datetime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }
        from_attributes = True

    """
    Create/Update 공통 필드를 묶기 위한 추상 베이스.
    """
    title: Optional[str]              = Field(None, max_length=100)
    description: Optional[str]        = Field(None, max_length=500)
    start_at: Optional[dt.datetime]
    end_at: Optional[dt.datetime]
    location: Optional[str]           = Field(None, max_length=100)

    # 유효성: start < end (둘 다 존재할 때만 체크)
    @validator("end_at")
    def validate_datetimes(cls, v, values):
        start = values.get("start_at")
        if start and v and start >= v:
            raise ValueError("end_at must be after start_at")
        return v

class EventCreateDTO(_EventBase):
    """
    • 생성 시에는 필수 필드로 변환
    • Optional → Required 로 오버라이드
    """
    title: str
    start_at: dt.datetime
    end_at: dt.datetime
    user_id: str = Field(..., description="이벤트 생성자 ID")

class EventUpdateDTO(_EventBase):
    """
    PATCH용 – 전부 Optional 그대로.
    """
    pass

class EventPublicDTO(_EventBase):
    """
    응답 전용 DTO. DB PK(id) 포함해 모든 필드가 Required.
    """
    id: int
    title: str
    description: Optional[str]
    start_at: dt.datetime
    end_at: dt.datetime
    location: Optional[str]

class EventRead(_EventBase):
    id: uuid.UUID
    calendar_id: Optional[str]
    user_id: str
    title: str
    description: Optional[str]
    start_at: dt.datetime
    end_at: dt.datetime
    location: Optional[str]
    # 필요한 필드를 더 추가하세요