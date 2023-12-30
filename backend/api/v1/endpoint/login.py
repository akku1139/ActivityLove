from starlette.requests import Request
from starlette.responses import Response

async def post(r:Request) -> Response:
  """
  {
    "responses": 
  }
  """
  return Response("response")
