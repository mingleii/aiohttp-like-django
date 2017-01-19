import importlib
import warnings

from aiohttp_like_django.conf import settings
from aiohttp_like_django.exceptions import AiohttpLikeDjangoWarning


async def start_background_tasks(app):
    app['background_tasks'] = []
    for app_name in settings.INSTALLED_APPS:
        try:
            app_model = importlib.import_module(app_name + ".tasks")
            app_tasks = app_model.__all__
        except (ImportError, NameError):
            warnings.warn('App {} has not tasks.py or "tasks.__all__"'.format(
                app_name), AiohttpLikeDjangoWarning)
            continue
        for each_task in app_tasks:
            app['background_tasks'].append(
                app.loop.create_task(getattr(app_model, each_task)(app)))


async def cleanup_background_tasks(app):
    for each_task in app['background_tasks']:
        each_task.cancel()


def setup_background_tasks(app):
    app.on_startup.append(start_background_tasks)
    app.on_cleanup.append(cleanup_background_tasks)
