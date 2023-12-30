from starlette.applications import Starlette
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles
from starlette.routing import Mount
from autoroute import autoroute

import api.v1

def index(request: Request, exc: HTTPException) -> FileResponse:
  return FileResponse("../frontend/build/200.html", media_type="text/html")

exception_handlers = {
  404: index
}

app = Starlette(
  routes=[
    autoroute("route", "/"),
    Mount('/api/v1', app=api.v1.api),
    Mount('/', app=StaticFiles(directory="../frontend/build", html=True))
  ],
  exception_handlers=exception_handlers
)
