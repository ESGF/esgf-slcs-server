# -*- coding: utf-8 -*-
"""
URL configuration for the Online CA Django app.
"""

__author__ = "Matt Pryor"
__copyright__ = "Copyright 2015 UK Science and Technology Facilities Council"

from django.conf.urls import url, include

from onlineca import views as onlineca_views

from . import views


app_name = 'esgf_slcs'
urlpatterns = [
    # Provide the /trustroots/ and /certificate/ endpoints under /onlineca
    url(r'^onlineca/', include([
        url(r'^trustroots/$', onlineca_views.trustroots, name="trustroots"),
        url(r'^certificate/$', views.certificate_basicauth, name="certificate_basicauth"),
    ])),
    # Also provide the /certificate/ endpoint under /oauth
    url(r'^oauth/', include([
        url(r'^certificate/$', views.certificate_oauth, name="certificate_oauth"),
    ])),
]
