from starlette.requests import Request
from starlette.responses import JSONResponse
from lib.nodeinfo import nodeinfo2

async def endpoint(request:Request) -> JSONResponse:
  return JSONResponse(nodeinfo2)
