import aiohttp_debugtoolbar
from aiohttp_debugtoolbar import toolbar_middleware_factory
from aiohttp_like_django.conf import settings


def setup_middlewares(app):
    if settings.INSTALLED_MIDDLEWARES:
        app.middlewares.extend(settings.INSTALLED_MIDDLEWARES)
    if settings.DEBUG:
        app.middlewares.append(toolbar_middleware_factory)
        aiohttp_debugtoolbar.setup(app)
