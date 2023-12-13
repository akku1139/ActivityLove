from starlette.requests import Request
from starlette.responses import JSONResponse

from info.config import conf

async def endpoint(request:Request) -> JSONResponse:
  return JSONResponse({
    "links": [
      {
        "rel": "http://nodeinfo.diaspora.software/ns/schema/2.0",
        "href": f'https://{conf["host"]}/nodeinfo/2.0'
      },
      {
        "rel": "http://nodeinfo.diaspora.software/ns/schema/2.1",
        "href": f'https://{conf["host"]}/nodeinfo/2.1'
      }
    ]
  })
