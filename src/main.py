from starlette.applications import Starlette
import autoroute

app = Starlette(
  debug=False,
  routes=autoroute.routes,
)
