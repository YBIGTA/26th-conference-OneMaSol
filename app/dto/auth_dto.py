"""
OAuth & JWT 관련 DTO 정의
------------------------
• 클라이언트 → 서버 : Google ID 토큰을 보낼 때 OAuthLoginDTO
• 서버 → 클라이언트 : JWT를 담은 TokenDTO
"""

from pydantic import BaseModel
from typing import Literal

class OAuthLoginDTO(BaseModel):
    """
    Google ID 토큰 한 가지만 받으면 되므로 필드가 단일.
    access_token 명으로 두면 다른 소셜로 확장할 때도 자연스러움.
    """
    access_token: str
    
class TokenDTO(BaseModel):
    """
    서버가 발급해 주는 JWT. token_type은 고정값 'bearer'.
    """
    access_token: str
    token_type: Literal["bearer"] = "bearer"
