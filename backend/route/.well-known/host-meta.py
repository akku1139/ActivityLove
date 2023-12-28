from starlette.requests import Request
from starlette.responses import PlainTextResponse

from info.config import conf

async def endpoint(request:Request) -> PlainTextResponse:
  return PlainTextResponse(
    '<?xml version="1.0"?>'
    '<XRD xmlns="http://docs.oasis-open.org/ns/xri/xrd-1.0">'
      '<Link rel="lrdd" type="application/xrd+xml" template="https://'+conf["host"]+'/.well-known/webfinger?resource={url}" />'
    '</XRD>',
    media_type="application/xrd+xml"
  )
