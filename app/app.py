from starlette.applications import Starlette
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles
from starlette.config import Config
from api import routes as api_routes
from view import routes as view_routes
import uvicorn

from tortoise import Tortoise, run_async


async def startup():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['models']}
    )


async def shutdown():
    await Tortoise.close_connections()


routes = [
    Mount('/api', routes=api_routes),
    Mount('/', routes=view_routes),
]

app = Starlette(routes=routes, on_startup=[startup], on_shutdown=[shutdown])

if __name__ == '__main__':
    uvicorn.run(app, reload=True)
