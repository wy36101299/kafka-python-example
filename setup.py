# -*- coding: utf-8 -*-
"""
    example
    ~~~~

    Just a simplest project to show you how to build your own project.

    :copyright: (c) 2015 by Chi-En Wu <jason2506@somewhere.com.tw>.
    :license: BSD.
"""

import uuid

from pip.req import parse_requirements  
from setuptools import setup, find_packages

import example


def requirements(path):  
    return [str(r.req) for r in parse_requirements(path, session=uuid.uuid1())]


setup(  
    name='example',
    version=example.__version__,
    author=example.__author__,
    author_email=example.__email__,
    url='http://your.host.name/example',
    description='Just a simplest project to show you how to build your own project.',
    long_description=__doc__,
    packages=find_packages(),
    install_requires=requirements('requirements.txt'),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Documentation',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)