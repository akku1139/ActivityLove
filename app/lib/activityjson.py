from starlette.responses import JSONResponse

class ActivityJSONResponse(JSONResponse):
  media_type: str = "application/activity+json"
  # 自動context
