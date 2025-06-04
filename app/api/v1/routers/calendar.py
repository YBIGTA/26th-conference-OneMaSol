# from fastapi import APIRouter, Depends, HTTPException
# from sqlmodel import Session, select
# from typing import List
# from app.dto.event_dto import Event
# from app.dto.event_dto import EventCreate, EventRead, EventUpdate
# from app.dependencies import get_session
# from uuid import UUID

# router = APIRouter(prefix="/calendar", tags=["Calendar"])


# @router.get("/events", response_model=List[EventRead])
# def read_events(session: Session = Depends(get_session)):
#     events = session.exec(select(Event)).all()
#     return events


# @router.post("/events", response_model=EventRead)
# def create_event(event: EventCreate, session: Session = Depends(get_session)):
#     new_event = Event.from_orm(event)
#     session.add(new_event)
#     session.commit()
#     session.refresh(new_event)
#     return new_event


# @router.get("/events/{event_id}", response_model=EventRead)
# def read_event(event_id: UUID, session: Session = Depends(get_session)):
#     event = session.get(Event, event_id)
#     if not event:
#         raise HTTPException(status_code=404, detail="Event not found")
#     return event


# @router.patch("/events/{event_id}", response_model=EventRead)
# def update_event(event_id: UUID, event_data: EventUpdate, session: Session = Depends(get_session)):
#     event = session.get(Event, event_id)
#     if not event:
#         raise HTTPException(status_code=404, detail="Event not found")
    
#     event_data_dict = event_data.dict(exclude_unset=True)
#     for key, value in event_data_dict.items():
#         setattr(event, key, value)

#     session.add(event)
#     session.commit()
#     session.refresh(event)
#     return event


# @router.delete("/events/{event_id}")
# def delete_event(event_id: UUID, session: Session = Depends(get_session)):
#     event = session.get(Event, event_id)
#     if not event:
#         raise HTTPException(status_code=404, detail="Event not found")
#     session.delete(event)
#     session.commit()
#     return {"ok": True, "message": "Event deleted"}
