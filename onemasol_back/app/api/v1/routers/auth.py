# routes/auth.py
from fastapi import APIRouter, Depends, Header
from app.api.v1.deps import get_session
from app.services.auth_service import oauth_login

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/oauth/google")
async def google_oauth_login(
    authorization: str = Header(...),  # "Bearer {token}" 를 통해 프론트에서 받은 토큰을 추출
    session=Depends(get_session)
):
    token = authorization.replace("Bearer ", "")
    result = await oauth_login(token, session) # Google OAuth 로그인 처리 함수로 전달
    return result
