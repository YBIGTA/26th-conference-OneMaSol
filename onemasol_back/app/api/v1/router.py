from fastapi import APIRouter
from .routers import auth, users, health, calendar 

router = APIRouter()
router.include_router(auth.router)
router.include_router(users.router)
router.include_router(calendar.router)
#router.include_router(documents.router)
#router.include_router(agent.router)

router.include_router(health.router)      # ← 테스트용 라우터


