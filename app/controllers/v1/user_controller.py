from fastapi.responses import JSONResponse
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi import status 
from requests_async.exceptions import ConnectionError as ConnectionException
from app.models.user_register import Register
from app.models.common import APIResponse

user_router = InferringRouter()

@cbv(user_router)
class UserController():
    def __init__(self):
        self.user_manage = "pass"
    @user_router.post("/register")
    async def register(self, payload: Register) -> APIResponse:

        try: 
            response = self.user_manager.register(payload)
            if "message" in response:
                return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, 
                                    content={"success": False, "message": "Email already exists"})
            return JSONResponse(
                status_code=status.HTTP_201_CREATED,
                content={"success":False, "message": "User Registration Successfully"}
            )
        except ConnectionException:
            return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"success": False, "message": "Invalid Registration"})    
               

