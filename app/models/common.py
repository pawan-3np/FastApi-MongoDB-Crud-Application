from fastapi_camelcase import CamelModel

class APIResponse(CamelModel):
    status: bool
    message: str

    