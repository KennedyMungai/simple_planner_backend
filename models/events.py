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

    class Config:
        """The config for the Event class"""
        schema_extra = {
            "example": {
                "title": "FastAPI book launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }
