# -*- coding: utf-8 -*-

from common.mymako import render_mako_context
from common.log import logger

# Create your views here.


def index(request):
    return render_mako_context(request, '/dbaux/index.html', { 'items': [] })

'''
    info = {
        'host': storage.db_info.host,
        'port': storage.db_info.port,
        'user': storage.db_info.user,
        'database': storage.db_info.database,
        'charset': storage.db_info.charset,
        'storage_name': storage.storage_name,
        'args': '',
    }
'''
