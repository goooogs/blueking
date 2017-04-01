# -*- coding: utf-8 -*-

from common.mymako import render_mako_context
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods,require_GET,require_POST
from dbhelpers import MySQLdbConnection, cm_cursor
from django.http import HttpResponse
import pymysql.cursors

from .models import ConnectionInfo, StorageRegistry
from .dbhelper import call_procedure


# Create your views here.


@require_GET
def index(request):
    """操作展示页面"""
    connections = ConnectionInfo.objects.all()
    content = {
        'connections': connections,
    }
    return render_mako_context(request, '/dbaux/index.html', content)


@require_POST
def call_procedure(request):
    """根据相关参数调用DB提供的存储过程接口"""
    # operator = request.user.username
    storage_id = request.POST['storage_id']
    args = request.POST['args']
    response = call_procedure(storage_id=storage_id, args=args)

    return HttpResponse(response)


@require_POST
def get_procedure_by_database_name(request):
    """获取数据库下的存储过程"""
    # operator = request.user.username
    storage = StorageRegistry.objects.get(id=request.POST['db'])
    connection_info = storage.connection_info
    sql_command = "select name from mysql.proc where db='%s' and type='procedure'" % connection_info.database
    pass


@require_POST
def get_procedure_arguments_by_storage_id(request):
    """获存储过程中定义的参数"""
    # operator = request.user.username
    pass


@require_http_methods(["GET", "POST"])
def connection_register(request):
    """注册数据库连接信息"""
    # operator = request.user.username
    pass


@require_http_methods(["GET", "POST"])
def storage_register(request):
    """注册存储过程"""
    # operator = request.user.username
    pass


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
