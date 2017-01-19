import pathlib
import logging.config
from pythonjsonlogger import jsonlogger

from example.middlewares import error_middleware

PROJECT_ROOT = pathlib.Path(__file__).parent.parent

PROJECT_NAME = PROJECT_ROOT.name

DEBUG = False

INSTALLED_APPS = [
    "demo",
]

DATABASES = {
    'default': {
        "drivername": "mysql",
        "database": "aiohttp_test",
        "username": "root",
        "password": "123456",
        "host": "192.168.92.134",
        "port": 3306,
        "minsize": 1,
        "maxsize": 5,
    }
}

INSTALLED_MIDDLEWARES = [
    error_middleware,
]

try:
    from local_conf import *
except ImportError:
    pass

try:
    from server_conf import *
except ImportError:
    pass

LOGGING_PATH = PROJECT_ROOT / "logs"

ACCESS_LOG_ENABLE = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'json': {
            '()': jsonlogger.JsonFormatter,
            'fmt': '%(levelname)s %(asctime)s %(process)d %(message)s'
        }
    },
    'handlers': {
        'access_file_log': {
            'level': 'DEBUG' if DEBUG else 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': str(LOGGING_PATH / "aio_run.log"),
            'formatter': 'json',
            'when': 'midnight'
        },
        'aiohttp_access': {
            'level': 'DEBUG' if DEBUG else 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': str(LOGGING_PATH / "aio_access.log"),
            'formatter': 'json',
            'when': 'midnight'
        }
    },
    'loggers': {
        'default': {
            'handlers': ['access_file_log'],
            'level': 'DEBUG' if DEBUG else 'INFO',
        },
        "aiohttp.access": {
            'handlers': ['aiohttp_access'],
            'level': 'DEBUG' if DEBUG else 'INFO',
        }
    }
}

logging.config.dictConfig(LOGGING)
