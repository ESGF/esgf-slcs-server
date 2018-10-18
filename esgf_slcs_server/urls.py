# -*- coding: utf-8 -*-
"""
URL configuration for the ESGF SLCS Server.
"""

__author__ = "Matt Pryor"
__copyright__ = "Copyright 2015 UK Science and Technology Facilities Council"

from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from oauth2_provider import views as oauth_views


urlpatterns = [
    url(r'^$',
        TemplateView.as_view(template_name = 'esgf_slcs_server/incorrect_usage.html'),
        name = 'home'),
    url(r'^admin/', admin.site.urls),
    # Use the built-in authentication views for login and logout
    url(r'^accounts/login$', auth_views.login, name = 'accounts_login'),
    url(r'^accounts/logout$', auth_views.logout,
                              { 'next_page' : settings.LOGIN_URL }, name = 'accounts_logout'),
    # We only provide the token-issuing OAuth URLs from oauth2_provider at custom endpoints
    # Applications are managed only via the admin interface
    url(r'^oauth/', include([
        url(r'^authorize$', oauth_views.AuthorizationView.as_view(), name="authorize"),
        url(r'^access_token$', oauth_views.TokenView.as_view(), name="token"),
    ])),
    # Include urls for the Online CA
    url(r'^', include('esgf_slcs.urls')),
]
