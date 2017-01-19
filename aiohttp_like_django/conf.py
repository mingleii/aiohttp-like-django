import importlib
import os

from aiohttp_like_django import default_settings


def collect_settings():
    settings = {}
    for setting in dir(default_settings):
        if setting.isupper():
            settings.update({setting: getattr(default_settings, setting)})

    user_mod_name = os.environ.get("AIOHTTP_LIKE_DJANGO_SETTINGS_MODULE")
    user_mod = importlib.import_module(user_mod_name)

    for setting in dir(user_mod):
        if setting.isupper():
            settings.update({setting: getattr(user_mod, setting)})

    return type("Settings", (object,), settings)


settings = collect_settings()
