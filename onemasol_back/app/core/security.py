from fastapi import Header, HTTPException
from datetime import datetime, timedelta
from jose import jwt
from app.core.config import settings

def get_token_from_header(authorization: str = Header(...)) -> str:
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid auth header")
    return authorization[len("Bearer "):]


def create_access_token(subject: str, expires_delta: timedelta = None):
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=60)  # 기본 1시간 유효

    to_encode = {"exp": expire, "sub": subject}
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm="HS256")

def decode_access_token(token: str):
    return jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])