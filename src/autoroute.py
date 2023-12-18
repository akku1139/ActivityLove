import glob
from starlette.routing import Route
# from starlette.responses import Response

routes:list = []
# forはスコープを作らない
methods:list = []
mod:dict = {}

for p in glob.glob("**/*.py", root_dir="route", recursive=True):
  with open("route/"+p, "r", encoding="utf-8") as fp:
    exec(fp.read(), mod)
  try:
    methods = mod["methods"]
  except KeyError:
    methods = ["GET"]

  path:str = "/" + (p.removesuffix(".py").replace("index", ""))

  routes.append(Route(path, endpoint=mod["endpoint"], methods=methods))
