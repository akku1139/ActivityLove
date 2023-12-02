from starlette.routing import Route
from starlette.requests import Request
from lib.activityjson import ActivityJSONResponse
from starlette.responses import RedirectResponse
from info.config import conf
from db import db

async def actor(request:Request) -> ActivityJSONResponse:
  return ActivityJSONResponse({
    "followers": f'https://{conf["host"]}/user/{request.path_params["id"]}/followers',
    "following": f'https://{conf["host"]}/user/{request.path_params["id"]}/following',
    "icon": {
    },
    "id": f'https://{conf["host"]}/user/{request.path_params["id"]}',
    "inbox": f'https://{conf["host"]}/user/{request.path_params["id"]}/inbox',
    "name": "Actorの名前",
    "outbox": f'https://{conf["host"]}/user/{request.path_params["id"]}/outbox',
    "preferredUsername": "",
    "publicKey": {
      # わからないので後で
    },
    "summary": "Actorの説明",
    "type": "Person",
    "url": f'https://{conf["host"]}/user/{request.path_params["id"]}',
    "discoverable": False
  }, media_type="application/xrd+xml")

routes = [
  # Route("/user/{id: str}/actor", actor)
  Route("/user/{id:str}/actor", actor)
]
