import glob
import typing
from starlette.routing import BaseRoute, Route

def autoroute(dir:str, mount:str) -> typing.Sequence[BaseRoute]:
  """
  Automatic routing for Starlette.

  Parameters
  ----------
  dir : str
    Directory to configure routing.
    example: if you want to specify "src/routes", pass "route".
  mount : str
    Path to mount the route.

  Returns
  -------
  routes : typing.Sequence[starlette.routing.BaseRoute]
    example: app = Starlette(routes=autoroute("route", "/"))
  """
  routes:typing.Sequence[BaseRoute] = []
  methods:list = []
  mod:dict = {}

  for p in glob.glob("**/*.py", root_dir=dir, recursive=True, include_hidden=True):
    with open("route/"+p, "r", encoding="utf-8") as fp:
      exec(fp.read(), mod) # pylint: disable=exec-used

    try:
      methods = mod["methods"]
    except KeyError:
      methods = ["GET"]

    path:str = "/" + (p.removesuffix(".py").replace("index", ""))

    routes.append(Route(path, endpoint=mod["endpoint"], methods=methods))

  return routes

routes = autoroute("route", "/")

"""
*.py files placed in the routing target directory will be automatically routed.
The template is as follows.

```py
from starlette.requests import Request
from starlette.responses import Response

## option
# methods = ["GET", "POST"]

async def endpoint(r:Request) -> Response:
  # Consider adding the OpenAPI schema in json format to your docstring.
  # https://www.starlette.io/schemas/
  return Response("response")
```
"""
