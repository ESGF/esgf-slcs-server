# -*- coding: utf-8 -*-
"""
This module contains utility functions for OpenID handling.
"""

from django.db import connections


def django_user_to_openid(user):
    """
    Converts a Django user to an OpenID using information in the ESGF user database.
    """
    with connections['userdb'].cursor() as cursor:
        cursor.execute('SELECT openid FROM "esgf_security.user" WHERE username = %s', [user.username])
        return cursor.fetchone()[0]
