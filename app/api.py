from starlette.routing import Route, Mount
from starlette.responses import JSONResponse
from models import Tournament
import logging


async def homepage(request):
    if request.method == 'POST':
        form = await request.form()
        await Tournament.create(name=form['name'])
        # return JSONResponse(dict(request.form))
    data = await Tournament.all()
    return JSONResponse({'Hello': 'world!', 'user': [d.name for d in data]})

routes = [
    Route('/homepage', homepage, methods=['GET', 'POST'])
]

