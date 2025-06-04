from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    google_Id: str = Field(index=True, unique=True, nullable=True)
    email: str = Field(index=True, unique=True, nullable=False)
    name: Optional[str]
    is_deleted: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    region: str= Field(default="Asia/Seoul", description="사용자 지역 정보")
    is_using: bool = Field(default=True)    
    proivder: str = Field(default="google", description="사용자 인증 제공자")
    status: str = Field(default="active", description="사용자 상태")
    caleandar_id: Optional[int] = Field(default=None)
    last_login_at: Optional[datetime] = Field(default_factory=datetime.utcnow)