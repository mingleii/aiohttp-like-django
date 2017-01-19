import importlib
import pathlib
import warnings

from aiohttp_like_django.conf import settings
from aiohttp_like_django.exceptions import AiohttpLikeDjangoWarning


def collect_urls():
    urlpatterns = []
    main_urls = importlib.import_module(settings.PROJECT_NAME + ".urls")
    urlprefix = getattr(main_urls, "urlprefix", {})
    for app_name in settings.INSTALLED_APPS:
        try:
            each_url = importlib.import_module(app_name + ".urls")
        except ImportError:
            warnings.warn('App %s has not urls.py' % app_name,
                          AiohttpLikeDjangoWarning)
            continue
        for pattern in each_url.urlpatterns:
            pattern[1] = urlprefix.get(app_name, "/" + app_name) + pattern[1]
            # pattern[3] = app_name, app_name + "_" + pattern[3]
            urlpatterns.append(pattern)
    return urlpatterns

urlpatterns = collect_urls()


def setup_routes(app):
    for each in urlpatterns:
        app.router.add_route(each[0], each[1], each[2], name=each[3])
    static_dir = settings.PROJECT_ROOT / "static"
    if static_dir.exists():
        app.router.add_static('/static/', name='static',
                              path=str(settings.PROJECT_ROOT / 'static'),
                              show_index=True, follow_symlinks=True)
