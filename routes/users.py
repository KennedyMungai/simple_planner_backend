"""The users route file"""
from fastapi import APIRouter, HTTPException, status

from models.user import User, UserSignIn


user_router = APIRouter(tags=["User"])

users = {}
