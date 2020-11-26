#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: HanQinXuan
# Mail: han981130@gmail.com
# Website: han1st.com
# Created Time:  2018-1-23 19:17:34
#############################################


from setuptools import setup, find_packages
import sys
import os

setup(
    name="loldataapi",
    version="0.1.0",
    keywords=("pip", "python", "lol", "wanplus", "api", "crawler"),
    description="team data & player data",
    long_description="team data & player data",
    license="MIT Licence",

    url="https://github.com/HanQinXuan/lol_event_api",
    author="HanQinXuan",
    author_email="han981130@gmail.com",

    package=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[]
)