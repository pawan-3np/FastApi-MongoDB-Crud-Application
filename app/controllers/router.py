from fastapi import APIRouter
from app.controllers.v1.user_controller import user_router

API_V1_STR = '/V1'
router = APIRouter()

router.include_router(user_router, prefix= API_V1_STR+"/user", tags=["user"])

