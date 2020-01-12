from starlette.routing import Route, Mount
from starlette.responses import JSONResponse


async def homepage(request):
    return JSONResponse({'Hello': 'world!'})

routes = [
    Route('/homepage', homepage)
]

