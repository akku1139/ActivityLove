import info.config as conf
import re

# 今の所ローカルの人のみ
def split(uri:str) -> tuple:
  host = conf.host
  # @{user}@host acct:{user}@host {user}@host
  if re.match(f"^(@|acct:|)[0-9a-zA-Z_\.]+@{conf.host}$", uri) is not None:
    user = uri.removeprefix("@").removeprefix("acct:").removesuffix("@"+conf.host)
  # @{user}
  elif re.match("^(@|acct:|)[0-9a-zA-Z_\.]+$", uri) is not None:
    user = uri.removeprefix("@").removeprefix("acct:")
  # {user}
  elif re.match("^[0-9a-zA-Z_\.]+$", uri) is not None:
    user = uri
  # https://host/user/{user} https://host/user/{user}/
  elif re.match("^https://"+conf.host+"/user/[0-9a-zA-Z_\.]+/?$", uri) is not None:
    user = uri.removeprefix("^https://"+conf.host+"/user/").removesuffix("/")
  else:
    user = ""
    # TODO 変なresource指定も受け入れる
  return (user, host,)
