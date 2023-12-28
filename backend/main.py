from starlette.applications import Starlette
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles
from starlette.routing import Mount
import autoroute

def index(request: Request, exc: HTTPException):
  return FileResponse("../frontend/build/200.html", media_type="text/html")

exception_handlers = {
  404: index
}

app = Starlette(
  debug=False,
  routes=[
    *autoroute.routes,
    Mount('/', app=StaticFiles(directory="../frontend/build", html=True), name="frontend")
  ],
  exception_handlers=exception_handlers
)
