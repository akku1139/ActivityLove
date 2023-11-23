from starlette.applications import Starlette
from starlette.responses import JSONResponse

import server

app = Starlette(debug=False, routes=server.routes)
