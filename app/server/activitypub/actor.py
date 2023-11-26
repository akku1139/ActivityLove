from starlette.routing import Route
from starlette.requests import Request
from starlette.responses import JSONResponse

import info.config as conf

async def actor(request:Request) -> JSONResponse:
  return JSONResponse({}, media_type="application/xrd+xml")

routes = [
  Route("/", actor)
]
