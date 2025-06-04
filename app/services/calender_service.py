# app/services/calendar_service.py
from fastapi import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession

from app.repositories.event_repository import EventRepository
from app.db.entity.event import Event
from app.schemas.dto_event import EventCreateDTO, EventUpdateDTO

class CalendarService:
    """
    캘린더 CRUD 전담
    """

    def __init__(self, repo: EventRepository = EventRepository()):
        self.repo = repo

    # ---- Read ----
    async def list(self, user_id: int, session: AsyncSession):
        return await self.repo.list_by_user(session, user_id)

    async def get(self, user_id: int, ev_id: int, session: AsyncSession):
        ev = await self.repo.get(session, ev_id)
        if not ev or ev.user_id != user_id:
            raise HTTPException(404, "Event not found")
        return ev

    # ---- Create ----
    async def create(self, user_id: int, payload: EventCreateDTO, session: AsyncSession):
        ev = Event(user_id=user_id, **payload.dict())
        return await self.repo.add(session, ev)

    # ---- Update ----
    async def update(self, user_id: int, ev_id: int, payload: EventUpdateDTO, session: AsyncSession):
        ev = await self.get(user_id, ev_id, session)
        for k, v in payload.dict(exclude_unset=True).items():
            setattr(ev, k, v)
        await session.commit(); await session.refresh(ev)
        return ev

    # ---- Delete ----
    async def delete(self, user_id: int, ev_id: int, session: AsyncSession):
        ev = await self.get(user_id, ev_id, session)
        await self.repo.delete(session, ev)
