from fastapi import Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound


async def handle_404(req: Request, exc: NoResultFound):
    return JSONResponse(
        status_code=404,
        content={'message': str(exc)}
    )


async def handle_409(req: Request, exc: IntegrityError):
    return JSONResponse(
        status_code=409,
        content={'message': 'duplicate data'}
    )

exception_handlers = {
    NoResultFound: handle_404,
    IntegrityError: handle_409
}
