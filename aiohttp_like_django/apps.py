from aiohttp_like_django.conf import settings
from aiohttp_like_django.exceptions import AppRegistryNotReady


def check_apps():
    for app_name in settings.INSTALLED_APPS:
        app_path = settings.PROJECT_ROOT / app_name
        if not app_path.exists():
            raise AppRegistryNotReady("App {} is not exists".format(app_name))
