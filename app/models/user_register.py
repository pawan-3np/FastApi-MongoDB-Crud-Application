from fastapi_camelcase import CamelModel
from pydantic import EmailStr
from typing import Optional

class Register(CamelModel):
    first_name: str
    last_naem: str
    email: EmailStr
    timezone : Optional[str]