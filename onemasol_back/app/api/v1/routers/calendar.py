# filepath: d:\onemasol\app\api\v1\routers\calendar.py
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import List
from uuid import UUID
from app.services.calender_service import CalendarService
from app.db.entity.event import Event
from app.dto.event_dto import EventCreateDTO, EventRead, EventUpdateDTO
from app.api.v1.deps import get_session
from app.utils.dto_utils import dump_with_formatted_datetime
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/calendar", tags=["Calendar"])
calendar_service = CalendarService()


@router.get("/events")
async def read_events(session: AsyncSession = Depends(get_session)):
    result = await calendar_service.read_events(session)
    return JSONResponse(content=result)

@router.post("/events")
async def create_event(event: EventCreateDTO, session: AsyncSession = Depends(get_session)):
    result = await calendar_service.create_event(event, session)
    return JSONResponse(content=result)

@router.get("/events/{event_id}")
async def read_event(event_id: UUID, session: AsyncSession = Depends(get_session)):
    result = await calendar_service.read_event(event_id, session)
    return JSONResponse(content=result)

@router.patch("/events/{event_id}")
async def update_event(event_id: UUID, dto: EventUpdateDTO, session: AsyncSession = Depends(get_session)):
    result = await calendar_service.update_event(event_id, dto, session)
    return JSONResponse(content=result)

@router.delete("/events/{event_id}")
async def delete_event(event_id: UUID, session: AsyncSession = Depends(get_session)):
    return await calendar_service.delete_event(event_id, session)