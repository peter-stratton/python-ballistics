========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/python-ballistics/badge/?style=flat
    :target: https://readthedocs.org/projects/python-ballistics
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/peter-stratton/python-ballistics.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/peter-stratton/python-ballistics

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/peter-stratton/python-ballistics?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/peter-stratton/python-ballistics

.. |requires| image:: https://requires.io/github/peter-stratton/python-ballistics/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/peter-stratton/python-ballistics/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/peter-stratton/python-ballistics/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/peter-stratton/python-ballistics

.. |version| image:: https://img.shields.io/pypi/v/ballistics.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/ballistics

.. |commits-since| image:: https://img.shields.io/github/commits-since/peter-stratton/python-ballistics/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/peter-stratton/python-ballistics/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/ballistics.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/ballistics

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/ballistics.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/ballistics

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/ballistics.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/ballistics


.. end-badges

A python package for calculating ballistics solutions.

* Free software: MIT license

Installation
============

::

    pip install ballistics

Documentation
=============

https://python-ballistics.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
