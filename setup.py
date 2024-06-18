#!/usr/bin/env python
from setuptools import setup, find_packages
from glob import glob

setup(
    name="projector",
    version="1.0",
    packages=find_packages(),
    #scripts=(['projector.py','projector_utils.py'] + (glob('editors/*')) + (glob('terminals/*'))),
    entry_points= {
        'console_scripts': [
            'projector = projector:main'
        ]
    }
)
