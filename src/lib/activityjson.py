from starlette.responses import JSONResponse
from starlette.background import BackgroundTask
import typing

class ActivityJSONResponse(JSONResponse):
  media_type: str = "application/activity+json"
  # 自動context
  def __init__(
    self,
    content: typing.Any,
    # 多分正しくないです。
    # https://scrapbox.io/activitypub/ActivityPub%E6%A8%99%E6%BA%96%E3%81%A7%E3%81%AF%E3%81%AA%E3%81%84well-known%E3%81%AA%E6%8B%A1%E5%BC%B5%E3%82%B9%E3%82%AD%E3%83%BC%E3%83%9E
    add_context: list = [],
    status_code: int = 200,
    headers: typing.Optional[typing.Mapping[str, str]] = None,
    media_type: typing.Optional[str] = None,
    background: typing.Optional[BackgroundTask] = None,
  ) -> None:
    super().__init__(content|
      {
        "@context": [
          "https://www.w3.org/ns/activitystreams",
          "https://w3id.org/security/v1"
        ] + add_context
      }, status_code, headers, media_type, background)
