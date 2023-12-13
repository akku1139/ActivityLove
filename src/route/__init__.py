from starlette.requests import Request
from starlette.responses import Response

async def endpoint(r:Request) -> Response:
  return Response("Root")
