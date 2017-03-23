# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns('home_application.views',
    # (r'^$', 'home'),
    (r'^$', 'index'),
    (r'^preview/$', 'preview'),
    (r'^dev-guide/$', 'dev_guide'),
    (r'^contactus/$', 'contactus'),
    (r'^daily_hot/$', 'get_daily_hot_list'),
    (r'^md5sum/$', 'file_md5sum'),
)
