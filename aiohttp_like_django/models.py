import importlib
import warnings

import sqlalchemy as sa
import sqlalchemy_utils as sau
from sqlalchemy.ext.declarative import declarative_base

from aiohttp_like_django.conf import settings
from aiohttp_like_django.exceptions import AiohttpLikeDjangoWarning


ModelBase = declarative_base()


class RecordNotFound(Exception):
    """Requested record in database was not found"""
    pass


async def init_db(app):
    conf = settings.DATABASES["default"]
    db_type = conf["drivername"].split("+")[0]
    if "mysql" == db_type:
        import aiomysql.sa as aiodb
    elif "postgresql" == db_type:
        import aiopg.sa as aiodb
    else:
        raise Exception("must set database config")
    engine = await aiodb.create_engine(
        db=conf['database'],
        user=conf['username'],
        password=conf['password'],
        host=conf['host'],
        port=conf['port'],
        minsize=conf['minsize'],
        maxsize=conf['maxsize'],
        charset="utf8",
        loop=app.loop)
    app['db'] = engine


async def close_db(app):
    app['db'].close()
    await app['db'].wait_closed()


def get_db_url(database):
    if database["username"]:
        db_auth = "%s:%s@%s:%s" % (database["username"], database["password"],
                                   database["host"], database["port"])
    else:
        db_auth = ""
    db_url = "%s://%s/%s" % (database["drivername"], db_auth,
                             database["database"])
    return db_url


def create_db():
    db_url = get_db_url(settings.DATABASES["default"])
    engine = sa.create_engine(db_url)
    for app_name in settings.INSTALLED_APPS:
        try:
            importlib.import_module(app_name + ".models")
        except ImportError:
            warnings.warn('App %s has not models.py' % app_name,
                          AiohttpLikeDjangoWarning)
            continue
    if not sau.database_exists(engine.url):
        sau.create_database(engine.url)
    ModelBase.metadata.create_all(engine)
    print("simple migrate over")
