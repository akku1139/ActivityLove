from info.config import conf
import re

# 今の所ローカルの人のみ
def split(uri:str) -> tuple:
  host: str = conf["host"]
  status: int = 200

  # @{user}@host acct:{user}@host {user}@host
  if re.match(rf'^(@|acct:|)[0-9a-zA-Z_\.]+@{conf["host"]}$', uri) is not None:
    user: str = uri.removeprefix("@").removeprefix("acct:").removesuffix("@"+conf["host"])

  # @{user}
  elif re.match(r"^(@|acct:|)[0-9a-zA-Z_\.]+$", uri) is not None:
    user: str = uri.removeprefix("@").removeprefix("acct:")

  # {user}
  elif re.match(r"^[0-9a-zA-Z_\.]+$", uri) is not None:
    user: str = uri

  # https://host/user/{user} https://host/user/{user}/
  elif re.match("^https://"+conf["host"]+r"/user/[0-9a-zA-Z_\.]+/?$", uri) is not None:
    user: str = uri.removeprefix("^https://"+conf["host"]+"/user/").removesuffix("/")

  # https://host/user/{user}/actor https://host/user/{user}/actor/
  elif re.match("^https://"+conf["host"]+r"/user/[0-9a-zA-Z_\.]+/?$", uri) is not None:
    user: str = uri.removeprefix("^https://"+conf["host"]+"/user/").removesuffix("/actor").removesuffix("/")

  else:
    user: str = ""
    status: int = 404
    # TODO 変なresource指定も受け入れる

  return (user, host, status,)
