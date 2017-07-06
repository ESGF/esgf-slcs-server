# -*- coding: utf-8 -*-
"""
This module contains utility functions for OpenID handling.
"""

from django.db import connections
from django.conf import settings
from psycopg2 import sql


def django_user_to_openid(user):
    """
    Converts a Django user to an OpenID using information in the ESGF user database.
    """
    with connections['userdb'].cursor() as cursor:

        cursor.execute(sql.SQL("SELECT openid FROM {}.{} WHERE username = %s")
                       .format(sql.Identifier(settings.ESGF_USERDB_USER_SCHEMA),
                               sql.Identifier(settings.ESGF_USERDB_USER_TABLE)),
                       [user.username])

        return cursor.fetchone()[0]
