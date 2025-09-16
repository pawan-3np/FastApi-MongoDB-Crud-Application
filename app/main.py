from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination

from app.config import config
from app.controllers.router import router

app = FastAPI(title= config.PROJECT_NAME, description="real world development course")

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials = True,
                   allow_methods=["*"],
                   allow_headers=["*"])

app.include_router(router)
add_pagination(app)


