import asyncio
import sys
from aiohttp import web

from aiohttp_like_django.apps import check_apps
from aiohttp_like_django.conf import settings
from aiohttp_like_django.middlewares import setup_middlewares
from aiohttp_like_django.models import init_db, close_db
from aiohttp_like_django.tasks import setup_background_tasks
from aiohttp_like_django.templates import load_templates
from aiohttp_like_django.urls import setup_routes


def init():
    if sys.platform.startswith('linux'):
        import uvloop
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    loop = asyncio.get_event_loop()
    middlewares = []
    app = web.Application(loop=loop, middlewares=middlewares)

    # if not settings.ACCESS_LOG_ENABLE:
    #     app.make_handler(access_log=None)
    check_apps()
    # setup Jinja2 template renderer
    load_templates(app)
    # create connection to the database
    app.on_startup.append(init_db)
    # shutdown db connection on exit
    app.on_cleanup.append(close_db)
    # setup views and routes
    setup_routes(app)
    setup_middlewares(app)
    setup_background_tasks(app)
    return app


def main(host, port):
    app = init()
    if not settings.ACCESS_LOG_ENABLE:
        extra_config = {"access_log": None}
    else:
        extra_config = {}
    web.run_app(app, host=host, port=port, **extra_config)
