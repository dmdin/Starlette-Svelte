from tortoise.models import Model
from tortoise import fields, Tortoise, run_async
from models import Tournament


async def create_instance():
    await Tournament.create(name='New Tournament')


async def init():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['models']}
    )
    await Tortoise.generate_schemas(True)
    await create_instance()


async def check_instances():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['models']}
    )
    tour = await Tournament.filter(name__contains='New').all()
    print([t.name for t in tour])


run_async(init())
run_async(check_instances())
