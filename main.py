"""The entrypoint to the application"""
import uvicorn
from fastapi import FastAPI

from routes.users import user_router

app = FastAPI()

app.include_router(user_router, prefix="/user")
