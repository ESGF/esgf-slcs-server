#!/usr/bin/env python2.7

import os, re

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

try:
    import esgf_slcs_server.__version__ as version
except ImportError:
    # If we get an import error, find the version string manually
    version = "unknown"
    with open(os.path.join(here, 'esgf_slcs_server', '__init__.py')) as f:
        for line in f:
            match = re.search('__version__ *= *[\'"](?P<version>.+)[\'"]', line)
            if match:
                version = match.group('version')
                break

with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

requires = [
    # For the time being, this is required by django_wsgi
    'django<1.10',
    'django-oauth-toolkit',
    'psycopg2==2.5.2',
    'django-wsgi',
    'ContrailOnlineCAService',
    'PasteDeploy',
    'django-bootstrap3',
]

if __name__ == "__main__":

    setup(
        name = 'esgf-slcs-server',
        version = version,
        description = 'SLCS server for ESGF',
        long_description = README,
        classifiers = [
            "Programming Language :: Python",
            "Framework :: Django",
            "Topic :: Internet :: WWW/HTTP",
            "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
        author = 'Matt Pryor',
        author_email = 'matt.pryor@stfc.ac.uk',
        url = 'http://esgf.llnl.gov/',
        keywords = 'web django esgf slcs oauth',
        packages = find_packages(),
        include_package_data = True,
        zip_safe = False,
        install_requires = requires,
    )
