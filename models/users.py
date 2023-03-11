"""The user model"""
from typing import List, Optional

from events import Event
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    """The template for the user Data

    Args:
        BaseModel (Class): Parent class
    """
    email: EmailStr
    password: str
    events: Optional[List[Event]]
