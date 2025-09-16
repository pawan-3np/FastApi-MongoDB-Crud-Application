from app.database.user_database import AuthenticationData
from app.models.user_register import Register
class UserManager():
    def __init__(self):
        self.user_database = AuthenticationData()

    async def register(self, payload: Register):
        where_clouse = {"email": payload}
        email_already_exist = self.user_database.get_by_where_clouse(where_clouse)
        if email_already_exist:
            return {'success':False, "message":f"email already exist"}
        
        response  = await self.user_database.register(payload)

        return response
