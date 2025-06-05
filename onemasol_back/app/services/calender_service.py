# app/services/calendar_service.py
from fastapi import HTTPException,Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi.responses import JSONResponse
from sqlmodel import select
from app.db.entity.event import Event
from app.dto.event_dto import EventCreateDTO, EventRead, EventUpdateDTO
from app.api.v1.deps import get_session
from app.utils.dto_utils import dump_with_formatted_datetime
from uuid import UUID
from datetime import datetime, timezone

class CalendarService:
    """
    캘린더 CRUD 전담
    """
    async def read_events(self, session: AsyncSession):
        result = await session.execute(select(Event))
        events = result.scalars().all()
        return [dump_with_formatted_datetime(EventRead.from_orm(e)) for e in events]
    
    async def create_event(seflf, event: EventCreateDTO, session: AsyncSession = Depends(get_session)):
        new_event = Event.from_orm(event)
        session.add(new_event)
        await session.commit()
        await session.refresh(new_event)
        return dump_with_formatted_datetime(EventRead.from_orm(new_event))
    
    async def read_event(self, event_id: UUID, session: AsyncSession):
        event = await session.get(Event, event_id)
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")
        return dump_with_formatted_datetime(EventRead.from_orm(event))

    async def update_event(self, event_id: UUID, event_data: EventUpdateDTO, session: AsyncSession):
        event = await session.get(Event, event_id)
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")

        for k, v in event_data.dict(exclude_unset=True).items():
            setattr(event, k, v)

        # created_at은 그대로 두고 updated_at만 다시 설정
        event.updated_at = datetime.now(timezone.utc)

        session.add(event)
        await session.commit()
        await session.refresh(event)
        return dump_with_formatted_datetime(EventRead.from_orm(event))

    async def delete_event(self, event_id: UUID, session: AsyncSession):
        event = await session.get(Event, event_id)
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")
        await session.delete(event)
        await session.commit()
        return {"ok": True, "message": "Event deleted"}
