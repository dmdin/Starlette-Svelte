from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles

routes = [
    Mount('/homepage', StaticFiles(directory='frontend/public', html=True)),
]
