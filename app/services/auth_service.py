# app/services/auth_service.py
from fastapi import HTTPException, status
from sqlmodel import Session, select
from app.db.entity.user import User
from app.core.security import create_access_token
from app.dto.auth_dto import OAuthLoginDTO, TokenDTO
from app.integrations.google import verify_token   # Google tokeninfo 호출
import httpx

async def oauth_login(access_token: str, session: Session) -> dict:
    # 토큰 검증
    token_info = await verify_token(access_token)
    if not token_info:
        raise HTTPException(status_code=401, detail="Invalid Google token")
    
    # Google OAuth 로그인 처리 함수
    user_info = await get_google_user_info(access_token)

    google_id = user_info["sub"]
    email = user_info.get("email")
    nickname = user_info.get("name", email.split("@")[0])

    stmt = select(User).where(User.google_user_id == google_id)
    user = session.exec(stmt).first()

    if not user:
        user = User(
            google_user_id=google_id,
            email=email,
            nickname=nickname,
        )
        session.add(user)
        session.commit()
        session.refresh(user)

    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token, "user": user}
    


async def get_google_user_info(access_token: str) -> dict:
    async with httpx.AsyncClient() as client:
        resp = await client.get(
            "https://www.googleapis.com/oauth2/v3/userinfo", # Google OAuth 인증 후 사용자 정보를 가져오는 Url
            headers={"Authorization": f"Bearer {access_token}"}
        )
        print("Google response:", resp.json())  # 응답 로깅 
        if resp.status_code != 200:
            raise HTTPException(status_code=401, detail="Invalid Google token")
        return resp.json()
