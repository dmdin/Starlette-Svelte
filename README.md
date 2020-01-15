# Starlette-Svelte-Tortoise template app :sparkles:
Simple example of full-stack async app with REST-API build on modern and powerful frameworks with Django like style to be used in other projects

### Used frameworks:
- [Svelte](https://svelte.dev/) : Cybernetically enhanced web apps
- [Starlette](https://starlette.io/) : The little ASGI framework that shines
- [Tortoise ORM](https://tortoise-orm.readthedocs.io/en/latest/) : Easy-to-use asyncio ORM inspired by Django

### Installation

```sh
$ cd app
$ pip install -r requirements.txt
```
Then init database. You can do this by running script db_init.py
```sh
$ python3 db_init.py
```
### Deployment
Now you are ready to run app. For more details you can check [Uvicorn documentation](https://www.uvicorn.org/deployment/)
```sh
uvicorn app:app
```
### That`s all! Your app is ready to shine :star2:

Maybe you have any idea or advice? Found bug? I am ready to get in touch with you and continue to improve this template!
##### Special thanks to [Erm](https://github.com/erm) for given [example](https://github.com/erm/starlette-svelte-example)

