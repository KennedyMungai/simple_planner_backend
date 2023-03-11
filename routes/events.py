"""The events routes file"""
from fastapi import APIRouter, Body, HTTPException, status
from models.events import Event
from typing import List


event_router = APIRouter(tags=["Events"])

events = []


@event_router.get("/")
async def retrieve_all_events() -> List[Event]:
    """The base route for the vent_router route

    Returns:
        List[Event]: Returns a list of events
    """
    return events
