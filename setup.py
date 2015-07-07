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


_name = 'pymongo_driver'
# TODO don't forget to change version in __init__
_version = '0.0.2'
_keywords = ('pymongo', 'driver', 'mongodb', 'egg')
_packages = find_packages()
_zip_safe = False
_description = 'Python Mongodb Driver'
_long_description = codecs.open('README.md', 'r', 'utf-8').read()
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
    # install_requires=_install_requires,
)


# vim:ts=4:sw=4
