from starlette.requests import Request
from starlette.responses import Response

methods = ["GET", "POST"]

async def endpoint(r:Request) -> Response:
  """
  """
  return Response("response")
