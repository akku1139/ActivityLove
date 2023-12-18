from starlette.responses import JSONResponse
from starlette.requests import Request
import lib.split_id

async def endpoint(request:Request) -> JSONResponse:
  # TODO クエリがなくても正しく動くように
  # ? 型品と入れたら壊れるのなぁぜなぁぜ?
  user: str
  host: str
  status: int
  user, host, status = lib.split_id.split(request.query_params['resource'])
  return JSONResponse({
    "subject": f"acct:{user}@{host}",
    "aliases": [
      f"https://{host}/user/{user}",
      f"https://{host}/user/{user}/actor"
    ],
    "links": [
      {
        "rel": "http://webfinger.net/rel/profile-page",
        "type": "text/html",
        "href": f"https://{host}/user/{user}"
      },
      {
        "rel": "self",
        "type": "application/activity+json",
        "href": f"https://{host}/user/{user}/actor"
      },
      {
        "rel": "http://ostatus.org/schema/1.0/subscribe",
        "template": "https://"+host+"/authorize_follow?uri={uri}"
      }
    ]
  }, media_type="application/jrd+json")
