#!/usr/bin/env python
# coding=utf-8
"""

author = "minglei.weng@smallsite.cn"
created = "2017/1/18 0018"
"""
import os
import sys


if __name__ == "__main__":
    os.environ.setdefault("AIOHTTP_LIKE_DJANGO_SETTINGS_MODULE",
                          "example.settings")
    from aiohttp_like_django.command import execute_from_command_line

    execute_from_command_line(sys.argv)
