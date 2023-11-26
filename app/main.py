from starlette.applications import Starlette

import server

app = Starlette(debug=False, routes=server.routes)
