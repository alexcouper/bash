#!/usr/bin/env python
# # coding: utf-8
from setuptools import find_packages, setup

with open('README.rst') as readme:
    long_description = readme.read()

setup(
    name='bash',
    description='Bash for Python',
    version='0.6',
    long_description=long_description,
    author='Alex Couper',
    author_email='info@alexcouper.com',
    url='https://github.com/alexcouper/bash',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        ('License :: OSI Approved :: GNU Library or Lesser '
         'General Public License (LGPL)'),
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
