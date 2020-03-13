from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
from starlette.routing import Mount
from api import routes as api_routes
from view import routes as view_routes
import uvicorn
from tortoise import Tortoise


async def startup():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['models']}
    )


async def shutdown():
    await Tortoise.close_connections()

middleware = [
    Middleware(CORSMiddleware, allow_origins=['*'])
]

routes = [
    Mount('/api', routes=api_routes),
    Mount('/', routes=view_routes),
]

app = Starlette(routes=routes, middleware=middleware, on_startup=[startup], on_shutdown=[shutdown])

if __name__ == '__main__':
    uvicorn.run('app:app', reload=True)
