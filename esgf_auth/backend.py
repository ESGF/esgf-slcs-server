# -*- coding: utf-8 -*-
"""
Module containing an authentication backend that authenticates users using the
ESGF user database.
"""

__author__ = "Matt Pryor"
__copyright__ = "Copyright 2016 UK Science and Technology Facilities Council"

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db import connections


class EsgfUserBackend(ModelBackend):
    """
    Django authentication backend that authenticates users using the ESGF user database.
    """
    def authenticate(self, username = None, password = None, **kwargs):
        """
        Attempt to authenticate the given username/password combination.
        """
        if not username or not password:
            return None
        # Try to retrieve a row from the ESGF user database with the given
        # username and password
        with connections['userdb'].cursor() as cursor:
            cursor.execute('SELECT * FROM "esgf_security.user" '
                           'WHERE username = %s AND password = MD5(%s)', (username, password))
            has_esgf_user = cursor.fetchone() is not None
        # If there is no ESGF user matching the username/password, we are done
        if not has_esgf_user:
            return None
        # Otherwise, return the user object associated with the username, creating
        # one if required
        # Note that we don't use get_or_create as we want to use create_user
        User = get_user_model()
        try:
            return User.objects.get(username = username)
        except User.DoesNotExist:
            return User.objects.create_user(username)
