import glob
from types import ModuleType
from starlette.routing import Route

routes:list = []
# forはスコープを作らない
methods:list = []

for p in glob.glob("**/*.py", root_dir="route", recursive=True):
  print(p)
  mod:ModuleType = __import__("route."+p.removesuffix(".py").replace('/', '.'))
  try:
    methods = mod.methods
  except:
    methods = ["GET"]
  path:str = p \
    .replace("well-known", ".well-known") \
    .replace("__init__", "/") \
    .replace("2_0", "2.0") \
    .replace("2_1", "2.1") \
    .replace("_json", ".json")
  routes.append(Route("/"+p, endpoint=mod.endpoint, methods=methods))
