# -*- coding: utf-8 -*-
"""
WSGI config for the ESGF SLCS Server.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'esgf_slcs_server.settings')

application = get_wsgi_application()
