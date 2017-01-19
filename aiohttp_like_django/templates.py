import aiohttp_jinja2
import jinja2

from aiohttp_like_django.conf import settings


def load_templates(app):
    template_dirs = []
    for app_name in settings.INSTALLED_APPS:
        template_dir = settings.PROJECT_ROOT / app_name / "templates"
        if template_dir.exists():
            template_dirs.append(template_dir._str)
    main_template = settings.PROJECT_ROOT / "templates"
    if main_template.exists():
        template_dirs.append(main_template._str)
    if template_dirs:
        aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(template_dirs))
