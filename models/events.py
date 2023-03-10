"""The file defining the model of the events data"""
from typing import List
from pydantic import BaseModel


class Event(BaseModel):
    """This is the template for the Event data

    Args:
        BaseModel (Class): The parent class of the Event class
    """
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str
