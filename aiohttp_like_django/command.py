import argparse

from aiohttp_like_django.conf import settings
from aiohttp_like_django.main import main
from aiohttp_like_django.models import create_db
from aiohttp_like_django.tools import to_host_port


def execute_from_command_line(argv=None):
    parser = argparse.ArgumentParser(description='Manage Aiohttp Server')
    parser.add_argument('-runserver', action="store", dest="runserver")
    parser.add_argument('-migrate', action='store_true', default=False)
    results = parser.parse_args(argv[1:])
    if results.runserver:
        host, port = to_host_port(results.runserver)
        main(host, port)
    elif results.migrate:
        create_db()
    else:
        print('Please use "-runserver" or "-migrate"')
