# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^functional/(?P<functional_id>\d+)/$', views.call_procedure, name='functional'),
    url(r'^system_config/list/(?P<object_type>\d+)/$', views.system_config_list, name='list'),
    url(r'^system_config/add/(?P<object_type>\d+)/$', views.system_config_add, name='add'),
    url(r'^system_config/delete/(?P<object_type>\d+)/(?P<id>\d+)/$', views.system_config_delete, name='delete'),
    url(r'^system_config/edit/(?P<object_type>\d+)/(?P<id>\d+)/$', views.system_config_edit, name='edit'),
    url(r'^system_config/detail/(?P<object_type>\d+)/(?P<id>\d+)/$', views.system_config_detail, name='detail'),
    url(r'^system_config/procedures/$', views.get_procedure_by_connection_info_id, name='procedures'),
]
