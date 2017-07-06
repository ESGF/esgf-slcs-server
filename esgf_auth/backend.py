# -*- coding: utf-8 -*-
"""
Module containing an authentication backend that authenticates users using the
ESGF user database.
"""

__author__ = "Matt Pryor"
__copyright__ = "Copyright 2016 UK Science and Technology Facilities Council"

from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db import connections
from passlib.hash import md5_crypt
from psycopg2 import sql


class EsgfUserBackend(ModelBackend):
    """
    Django authentication backend that authenticates users using the ESGF user database.
    """

    def authenticate(self, username=None, password=None, **kwargs):
        """
        Attempt to authenticate the given username/password combination.
        """
        if not username or not password:
            return None
        #  Try to retrieve a row from the ESGF user database with the given
        #  username and password
        with connections['userdb'].cursor() as cursor:

            cursor.execute(sql.SQL("SELECT password FROM {}.{} WHERE username = %s")
                           .format(sql.Identifier(settings.ESGF_USERDB_USER_SCHEMA),
                                   sql.Identifier(settings.ESGF_USERDB_USER_TABLE)),
                           [username])
            row = cursor.fetchone()

            # Check if user exists
            if row is not None:
                # Verify password matches
                has_esgf_user = md5_crypt.verify(password, row[0])
            else:
                has_esgf_user = False

        #  If there is no ESGF user matching the username/password, we are done

        if not has_esgf_user:
            return None
        #  Otherwise, return the user object associated with the username, creating
        #  one if required
        #  Note that we don't use get_or_create as we want to use create_user
        User = get_user_model()
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return User.objects.create_user(username)
