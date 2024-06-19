#!/usr/bin/env python
from setuptools import setup, find_packages
from glob import glob

setup(
    name="projector",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,
    scripts=["projector.py"] + glob("utils/*)"),
)
