from starlette.applications import Starlette
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles
from api import routes as api_routes
from view import routes as view_routes
import uvicorn


async def startup():
    pass


async def shutdown():
    pass


routes = [
    # Mount('/', StaticFiles(directory='frontend/public', html=True)),\
    Mount('/api', routes=api_routes),
    Mount('/', routes=view_routes),

    # Mount('/static', StaticFiles(directory='static'))
]

app = Starlette(routes=routes, on_startup=[startup], on_shutdown=[shutdown])

if __name__ == '__main__':
    uvicorn.run(app, reload=True)
