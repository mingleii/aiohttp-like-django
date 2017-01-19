#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: xingming
# Mail: huoxingming@gmail.com
# Created Time:  2015-12-11 01:25:34 AM
#############################################


from setuptools import setup, find_packages

setup(
    name="aiohttp-like-django",
    version="1.0.1",
    author="minglei.weng",
    author_email="minglei.weng@smallsite.cn",
    keywords=("aiohttp", "django"),
    description="Coding aiohttp like django",
    long_description="You can coding aiohttp like django",
    license='Apache 2',

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=["aiohttp"]
)
