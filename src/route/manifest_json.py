from starlette.requests import Request
from starlette.responses import JSONResponse
from info.config import conf

async def endpoint(request:Request) -> JSONResponse:
  return JSONResponse({
    "short_name": conf["name"],
    "name": conf["name"],
    "start_url":"/",
    "display": "standalone",
    "background_color": conf["background_color"],
    "theme_color": conf["theme_color"],
    "icons":[
      # TODO 直す
      {"src":"https://media.nijimiss.app/assets/app_x192.png","sizes":"192x192","type":"image/png","purpose":"maskable"},
      {"src":"https://media.nijimiss.app/assets/app_x512.png","sizes":"512x512","type":"image/png","purpose":"maskable"},
      {"src":"/static-assets/splash.png","sizes":"300x300","type":"image/png","purpose":"any"}
    ],
    "share_target":{
      "action":"/share/",
      "method":"GET",
      "enctype":"application/x-www-form-urlencoded",
      "params":{
        "title":"title",
        "text":"text",
        "url":"url"
      }
    }
  })
