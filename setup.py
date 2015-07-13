#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :


try:
    from setuptools import setup, find_packages
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, find_packages

import os
import sys
import codecs
import re
import ast

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('pymongo_driver/__init__.py', 'rb') as f:
    _version = str(ast.literal_eval(_version_re.search(f.read().decode('utf-8')).group(1)))

_name = 'pymongo_driver'
_keywords = ('pymongo', 'driver', 'mongodb', 'egg')
_packages = find_packages()
_zip_safe = False
_description = 'Python Mongodb Driver'
_long_description = codecs.open('README.rst', 'r', 'utf-8').read()
_author = 'Combo'
_author_email = 'combo@desvp.com'
_license = 'The MIT License'
_platforms = 'Independant'
_url = 'http://lecly.github.io/pymongo-driver/'
_classifiers = [
    'Development Status :: Production/Stable',
    'Environment :: Other Environment',
    'Intended Audience :: Developers',
    'License :: The MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Database',
    'Topic :: Utilities',
    'Topic :: Software Development :: Libraries :: Python Modules',
]
_install_requires = [
    'pep8>=1.6',
    'pymongo>=2.8',
]

setup(
    name=_name,
    version=_version,
    keywords=_keywords,
    packages=_packages,
    zip_safe=_zip_safe,
    description=_description,
    long_description=_long_description,
    author=_author,
    author_email=_author_email,
    license=_license,
    platforms=_platforms,
    url=_url,
    classifiers=_classifiers,
    install_requires=_install_requires,
)


# vim:ts=4:sw=4
