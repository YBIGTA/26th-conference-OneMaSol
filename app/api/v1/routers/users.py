from fastapi import APIRouter, Depends
from fastapi import HTTPException
from sqlmodel import Session
from sqlmodel.ext.asyncio.session import AsyncSession
from app.api.v1.deps import get_session, get_current_user
from app.services.user_service import update_me, delete_me
from app.dto.user_dto import UserMeUpdateDTO, UserPublicDTO, UserCreateDTO
from app.db.entity.user import User
import logging

logger = logging.getLogger("uvicorn.error")

router = APIRouter(prefix="/users", tags=["Users"])

@router.patch("/me", response_model=UserPublicDTO)
def update_user_me(
    dto: UserMeUpdateDTO,
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user)
):
    return update_me(user, dto, session)

@router.delete("/me")
def delete_user_me(
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user)
):
    delete_me(user, session)
    return {"ok": True, "message": "User deleted"}

@router.post("/signup", response_model=UserPublicDTO)
async def signup_user(
    dto: UserCreateDTO,
    session: AsyncSession = Depends(get_session)
):
    # 새로운 사용자 생성
    user = User(
        email=dto.email,
        nickname=dto.name,
        google_user_id=None,
        is_deleted=False,
    )
    session.add(user)
    try:
        await session.commit()      # await 추가
        await session.refresh(user)
    except Exception:
        logger.exception("회원가입 중 에러 발생")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    return user
