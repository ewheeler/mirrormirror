#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8

from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    url(r'^$', views.index),
)
