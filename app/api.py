from starlette.routing import Route, Mount
from starlette.responses import JSONResponse
from models import Tournament


async def homepage(request):
    if request.method == 'POST':
        form = await request.form()
        await Tournament.create(name=form['name'])
    data = await Tournament.all()
    return JSONResponse([d.name for d in data])

routes = [
    Route('/', homepage, methods=['GET', 'POST'])
]

