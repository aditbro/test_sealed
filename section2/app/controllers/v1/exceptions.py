from app.db import session
from fastapi import Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound


async def handle_404(req: Request, exc: NoResultFound):
    session.rollback()
    return JSONResponse(
        status_code=404,
        content={'message': str(exc)}
    )


async def handle_409(req: Request, exc: IntegrityError):
    session.rollback()
    return JSONResponse(
        status_code=409,
        content={'message': 'duplicate data'}
    )


async def handle_400(req: Request, exc: AttributeError):
    session.rollback()
    return JSONResponse(
        status_code=400,
        content={'message': 'bad request parameters'}
    )

exception_handlers = {
    NoResultFound: handle_404,
    IntegrityError: handle_409,
    AttributeError: handle_400
}
