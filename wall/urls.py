#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8

import os

from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    # serve assets via django, during development
    url(r'^assets/js/(?P<path>.*)$', "django.views.static.serve",
    {"document_root": os.path.dirname(__file__) + "/static/javascripts"}),
    url(r'^$', views.index),
    url(r'^tree$', views.show_tree),
    url(r'^voyager$', views.show_voyager),
)
