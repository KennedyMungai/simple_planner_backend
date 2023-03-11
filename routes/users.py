"""The users route file"""
from fastapi import APIRouter, HTTPException, status

from models.users import User, UserSignIn


user_router = APIRouter(tags=["User"])

users = {}


@user_router.post('/signup')
async def sign_new_user(data: NewUser) -> dict:
    """The user sign in endpoint

    Args:
        data (Class): The data template for the new user

    Returns:
        dict: A response to calling the API endpoint
    """
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="The user with the supplied username exists"
        )

    users[data.email] = data

    return {
        "Message": "User successfully registered"
    }
