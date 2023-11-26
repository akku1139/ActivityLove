from starlette.routing import Route
from starlette.requests import Request
from starlette.responses import JSONResponse

from info.config import conf
import info.software as soft
import info.statistics as stat

async def nodeinfo(request:Request) -> JSONResponse:
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

nodeinfo2: dict = {
  "version": "2.1",
  "software": {
    "name": soft.name,
    "version": soft.version,
    "repository": soft.repository,
    "homepage": soft.homepage
  },
  "protocols": [
    "activitypub"
  ],
  "services": {
    # TODO RSSとかAtomとか対応したいね。
    "inbound": [],
    "outbound": []
  },
  "openRegistrations": conf["open_registrations"],
  "usage": {
    "users": {
      "total": stat.users,
      "activeHalfyear": None,
      "activeMonth": None
    },
    "localPosts": stat.posts,
    "localComments": 0
  },
  "metadata": {
    "nodeName": conf["name"],
    "nodeDescription": conf["description"],
    "maxNoteTextLength": conf["max_note_text_length"],
    "proxyAccountName": conf["proxy_account_name"],
    "themeColor": conf["theme_color"],
    "maintainer": {
      "name": conf["maintainer_name"],
      "email": conf["maintainer_email"]
    }
  },
}


# だいたい同じなので同じものを返す。
# 1系を使っているサーバーは知らないので問題なし。

# https://github.com/jhass/nodeinfo/blob/main/schemas/2.0/schema.json
# https://github.com/jhass/nodeinfo/blob/main/schemas/2.1/schema.json
async def v2(request:Request) -> JSONResponse:
  return JSONResponse(nodeinfo2)


routes = [
  Route("/.well-known/nodeinfo", nodeinfo),
  Route("/nodeinfo/2.0", v2),
  Route("/nodeinfo/2.1", v2),
]
