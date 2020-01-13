from tortoise.models import Model
from tortoise import fields, Tortoise, run_async
from models import Tournament


async def create_instance():
    await Tournament.create(name='New Tournament')
    # tour = await Tournament.filter(name__contains='New').first()
    # print(tour)
    # tournament = Tournament(name='New Tournament')
    # await tournament.save()

    tour = await Tournament.filter(name__contains='New').first()
    print(tour.name)


async def init():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['models']}
    )
    await Tortoise.generate_schemas(True)
    await create_instance()
# run_async(init())


async def test_fetch():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['models']}
    )
    tour = await Tournament.filter(name__contains='New').all()
    print([t.name for t in tour])

run_async(test_fetch())

