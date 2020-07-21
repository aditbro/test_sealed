from pydantic import BaseModel


class NotFound(BaseModel):
    message: str


class Forbidden(BaseModel):
    message: str


class Success(BaseModel):
    message: str


responses = {
    200: {
        "model": Success
    },
    404: {
        "model": NotFound
    },
    403: {
        "model": Forbidden
    }
}
