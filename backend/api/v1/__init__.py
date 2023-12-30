from autoroute import autoroute
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import Response

def notfound(request: Request, exc: HTTPException) -> Response:
  return Response("Unknown API endpoint.", status_code=404)

exception_handlers = {
  404: notfound
}

api = Starlette(
  debug=False,
  routes=[
    autoroute("endpoint", "/"),
  ],
  exception_handlers=exception_handlers
)
