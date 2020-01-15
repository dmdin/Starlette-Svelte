from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles

routes = [
    Mount('/', StaticFiles(directory='frontend/public', html=True)),
]
