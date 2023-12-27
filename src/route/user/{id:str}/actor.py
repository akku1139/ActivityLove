from starlette.requests import Request
from lib.activityjson import ActivityJSONResponse
from starlette.responses import Response, RedirectResponse
from info.config import conf
from lib.local import find_user

async def endpoint(request:Request) -> ActivityJSONResponse | Response:
  if find_user(request.path_params["id"]):
    return ActivityJSONResponse({
      "followers": f'https://{conf["host"]}/user/{request.path_params["id"]}/followers',
      "following": f'https://{conf["host"]}/user/{request.path_params["id"]}/following',
      "icon": {
      },
      "id": f'https://{conf["host"]}/user/{request.path_params["id"]}/actor',
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
      "discoverable": False # これもよくわからん
    }, media_type="application/activity+json")
  else:
    return Response("User not found", status_code=404)
