# # Test용 

# # app/api/v1/routers/health.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.v1.deps import get_session
# from sqlalchemy import text
router = APIRouter()

# @router.get("/health/db")
# async def health_check_db(session: AsyncSession = Depends(get_session)):
#     try:
#         result = await session.execute(text("SELECT 1"))
#         return {"db": "ok", "result": result.scalar()}
#     except Exception as e:
#         return {"db": "error", "detail": str(e)}


from sqlalchemy import text

@router.get("/debug/db")
async def debug_db(session: AsyncSession = Depends(get_session)):
    try:
        result = await session.execute(text("SELECT current_database()"))
        dbname = result.scalar()
        return {"connected_to": dbname}
    except Exception as e:
        import traceback
        traceback.print_exc()
        return {"error": str(e)}