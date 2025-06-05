# filepath: d:\onemasol\app\api\v1\routers\calendar.py
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import List
from uuid import UUID

from app.db.entity.event import Event
from app.dto.event_dto import EventCreateDTO, EventRead, EventUpdateDTO
from app.api.v1.deps import get_session
from app.utils.dto_utils import dump_with_formatted_datetime
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/calendar", tags=["Calendar"])


# @router.get("/events", response_model=List[EventRead])
# async def read_events(session: AsyncSession = Depends(get_session)):
#     result = await session.execute(select(Event))
#     events = result.scalars().all()
#     return events
@router.get("/events")
async def read_events(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Event))
    events = result.scalars().all()
    formatted = [
        dump_with_formatted_datetime(EventRead.from_orm(event)) for event in events
    ]
    return JSONResponse(content=formatted)


@router.post("/events")
async def create_event(event: EventCreateDTO, session: AsyncSession = Depends(get_session)):
    new_event = Event.from_orm(event)
    session.add(new_event)
    await session.commit()
    await session.refresh(new_event)
    return JSONResponse(content=dump_with_formatted_datetime(EventRead.from_orm(new_event)))


@router.get("/events/{event_id}")
async def read_event(event_id: UUID, session: AsyncSession = Depends(get_session)):
    event = await session.get(Event, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return JSONResponse(content=dump_with_formatted_datetime(EventRead.from_orm(event)))


@router.patch("/events/{event_id}")
async def update_event(event_id: UUID, event_data: EventUpdateDTO, session: AsyncSession = Depends(get_session)):
    event = await session.get(Event, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    
    event_data_dict = event_data.dict(exclude_unset=True)
    for key, value in event_data_dict.items():
        setattr(event, key, value)

    session.add(event)
    await session.commit()
    await session.refresh(event)
    return JSONResponse(content=dump_with_formatted_datetime(EventRead.from_orm(event)))


@router.delete("/events/{event_id}")
async def delete_event(event_id: UUID, session: AsyncSession = Depends(get_session)):
    event = await session.get(Event, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    await session.delete(event)
    await session.commit()
    return {"ok": True, "message": "Event deleted"}