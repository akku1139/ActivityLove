import glob
import typing
from starlette.routing import BaseRoute, Route, Mount

def autoroute(dir:str, path:str="/") -> typing.Sequence[BaseRoute]:
  """
  Automatic routing for Starlette.

  Parameters
  ----------
  dir : str
    Directory to configure routing.
    Must not start with "/".
    If you don't do that, it will search from the root of the file system.
    example: if you want to specify "src/routes", pass "route".
  path : str
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
    with open(dir+"/"+p, "r", encoding="utf-8") as fp:
      exec(fp.read(), mod) # pylint: disable=exec-used

    route_path:str = "/" + (p.removesuffix(".py").replace("index", ""))

    if "endpoint" in mod: # Style routing using endpoints, methods.
      endpoint = mod["endpoint"]
      if "methods" in mod:
        methods = mod["methods"]
      else:
        methods = ["GET"]
      routes.append(Route(route_path, endpoint, methods=methods))

    else: # Routing by HTTP method name.
      for method in ["GET", "HEAD", "POST", "PUT", "PATCH", "DELETE"]:
        if method.lower() in mod:
          endpoit = mod[method.lower()]
          routes.append(Route(route_path, endpoint, methods=[method]))

  if path == "/":
    return routes
  else:
    return [Mount(path, routes=routes)]

routes = \
  autoroute("route", "/") + \
  autoroute("api/v1", "/api/v1")

"""
*.py files placed in the routing target directory will be automatically routed.
The template is as follows.

```py
from starlette.requests import Request
from starlette.responses import Response

### Must choose one method or the other.

### def endpoint style
## option
# methods = ["GET", "POST"]

async def endpoint(r:Request) -> Response:
  # Consider adding the OpenAPI schema in json format to your docstring.
  # https://www.starlette.io/schemas/
  return Response("response")

### HTTP method style
async def get(r:Request) -> Response:
  # Consider adding the OpenAPI schema in json format to your docstring.
  # https://www.starlette.io/schemas/
  return Response("response")

async def post(r:Request) -> Response:
  # Consider adding the OpenAPI schema in json format to your docstring.
  # https://www.starlette.io/schemas/
  return Response("response")
```
"""
