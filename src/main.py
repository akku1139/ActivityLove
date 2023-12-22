from starlette.applications import Starlette
import autoroute

from contextlib import asynccontextmanager
@contextlib.asynccontextmanager
async def lifespan(app):
  await db.connect()
  yield
  await db.disconnect()


app = Starlette(
  debug=False,
  routes=autoroute.routes,
  lifespan=lifespan,
)
