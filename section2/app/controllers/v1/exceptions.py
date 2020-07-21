from fastapi import Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm.exc import NoResultFound


async def handle_404(req: Request, exc: NoResultFound):
    return JSONResponse(
        status_code=404,
        content={'message': str(exc)}
    )

exception_handlers = {
    NoResultFound: handle_404
}
