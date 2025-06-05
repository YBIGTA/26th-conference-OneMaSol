from sqlmodel import Session, select
from app.db.entity.user import User
from app.core.security import create_access_token
from app.services.auth_service import get_google_user_info
from app.integrations.google import verify_token
from app.dto.user_dto import UserSignupDTO, UserLoginDTO, UserMeUpdateDTO
from fastapi import HTTPException

async def signup(dto: UserSignupDTO, session: Session):
    # Google 사용자 정보 가져오기
    user_info = await get_google_user_info(dto.access_token)
    google_id = user_info["sub"]

    # 이미 가입된 사용자인지 확인
    existing = session.exec(select(User).where(User.google_user_id == google_id)).first()
    if existing:
        raise HTTPException(status_code=400, detail="Already signed up")

    # 기가입자가 아닌경우 사용자 등록 처리
    user = User(
        google_user_id=google_id,
        email=user_info.get("email"),
        nickname=user_info.get("name"),
    )
    session.add(user)
    session.commit()
    session.refresh(user)

    # 토큰 생성을 통해 로그인할 때 해당 토큰으로 사용자 인증 처리
    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token, "user": user}

async def login(dto: UserLoginDTO, session: Session):
    # Google 토큰 검증
    token_info = await verify_token(dto.access_token)
    if not token_info:
        raise HTTPException(status_code=401, detail="Invalid Google token")

    google_id = token_info["sub"]

    user = session.exec(select(User).where(User.google_user_id == google_id)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token, "user": user}

def update_me(user: User, dto: UserMeUpdateDTO, session: Session):
    for key, value in dto.dict(exclude_unset=True).items():
        setattr(user, key, value)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def delete_me(user: User, session: Session):
    user.is_deleted = True
    session.add(user)
    session.commit()
