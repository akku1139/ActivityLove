import glob
from types import ModuleType
from starlette.routing import Route

special_route:dict = {
  "well-known": ".well-known",
  "__init__": "",
  "2_0": "2.0",
  "2_1": "2.1",
  "_json": ".json",
}

routes:list = []
# forはスコープを作らない
methods:list = []

for p in glob.glob("**/*.py", root_dir="route", recursive=True):
  mod:ModuleType = __import__("route."+p.removesuffix(".py").replace('/', '.'))
  try:
    methods = mod.methods
  except:
    methods = ["GET"]
  path:str = "/" + (p.removesuffix(".py"))
  for r in special_route:
    path = path.replace(r, special_route[r])
  routes.append(Route(path, endpoint=mod.endpoint, methods=methods))
