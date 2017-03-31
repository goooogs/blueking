# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns('dbaux.views',
    (r'^$', 'index'),
)
