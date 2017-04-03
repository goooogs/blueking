# -*- coding: utf-8 -*-

import json
from common.mymako import render_mako_context
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.http import HttpResponse
from django.template import loader
from django.db.models import ObjectDoesNotExist
from .models import ConnectionInfo, StorageRegistry, StorageArgument
from . import dbhelper

# Create your views here.
"""
允许的操作
1: 操作 ConnectionInfo
2: 操作 StorageRegistry
"""
ALLOWED_OBJECT_TYPES = ("1", "2")
"""
允许的操作方法
list: 获取对象列表
add: 添加
delete: 删除
edit: 修改
"""
ALLOWED_ACTIONS = ("list", "add", "delete", "edit")


@require_GET
def index(request):
    """
    首页界面展示
    """
    # storage_all = StorageRegistry.objects.all()
    # content = {
    #     'items': storage_all,
    # }
    return render_mako_context(request, '/dbaux/index.html')


@require_GET
def system_config_list(request, object_type):
    """
    获取配置列表
    """
    illegal_error_message = u'不合法的操作'
    response = {}

    if object_type not in ALLOWED_OBJECT_TYPES:
        response['result'] = False
        response['message'] = illegal_error_message
        return HttpResponse(response)

    if object_type == "1":
        """获取 ConnectionInfo 配置列表"""
        obj = ConnectionInfo
        title = '添加数据库连接'
        template_file = 'dbaux/connection_info_list_tmpl.html'
        response['result'] = True
    elif object_type == "2":
        """获取 StorageRegistry 配置列表"""
        obj = StorageRegistry
        title = '注册存储过程'
        template_file = 'dbaux/storage_list_tmpl.html'
        response['result'] = True
    else:
        response['result'] = False
        response['message'] = illegal_error_message

    if response['result']:
        items = obj.objects.all()
        content = {
            'title': title,
            'object_type': object_type,
            'items': items,
        }
        t = loader.get_template(template_file)
        response['data'] = t.render(content, request)

    return HttpResponse(json.dumps(response))


@require_http_methods(['GET', 'POST'])
def system_config_add(request, object_type):
    """
    添加配置
    """
    illegal_error_message = u'不合法的操作'
    response = {}

    if object_type not in ALLOWED_OBJECT_TYPES:
        response['result'] = False
        response['message'] = illegal_error_message
        return HttpResponse(response)

    if request.method == "GET":
        items = obj = None
        if object_type == "1":
            """添加 ConnectionInfo"""
            title = '添加数据库连接'
            template_file = 'dbaux/connection_info_add_tmpl.html'
            response['result'] = True
        elif object_type == "2":
            """添加 StorageRegistry"""
            obj = ConnectionInfo  # 供添加页面选择配置的数据库连接
            title = '注册存储过程'
            template_file = 'dbaux/storage_add_tmpl.html'
            response['result'] = True
        else:
            response['result'] = False
            response['message'] = illegal_error_message

        if response['result']:
            items = obj.objects.all() if obj else None
            content = {
                'title': title,
                'object_type': object_type,
                'items': items,
            }
            t = loader.get_template(template_file)
            response['data'] = t.render(content, request)

        return HttpResponse(json.dumps(response))
    elif request.method == "POST":
        if object_type == "1":
            """添加 ConnectionInfo"""
            name = request.POST['name'].replace('&nbsp;', ' ')
            host = request.POST['host']
            port = int(request.POST['port'])
            user = request.POST['user']
            password = request.POST['password']
            database = request.POST['database']
            charset = request.POST['charset']
            ConnectionInfo.objects.create(name=name, host=host, port=port, user=user, password=password,
                                          database=database, charset=charset)
            response['result'] = True
        elif object_type == "2":
            """添加 StorageRegistry"""
            connection_info_id = int(request.POST['connection_info_id'])
            name = request.POST['name'].replace('&nbsp;', ' ')
            description = request.POST['description'].replace('&nbsp;', ' ')
            storage_name = request.POST['storage_name']
            args = json.loads(request.POST['args'])

            try:
                connection_info = ConnectionInfo.objects.get(id=connection_info_id)
                storage = connection_info.storageregistry_set.create(name=name, description=description,
                                                                     storage_name=storage_name)
                for arg_index in ["%s" % i for i in range(1, len(args) + 1)]:
                    for k, v in args[arg_index].items():
                        storage.storageargument_set.create(index=arg_index, name=k, description=v.replace('&nbsp;', ' '))
                        break
                response['result'] = True
            except ObjectDoesNotExist:
                response['result'] = False
                response['message'] = u'添加失败：指定的数据库连接不存在！'
        elif object_type == "3":
            """添加 StorageArgument"""
            storage_id = int(request.POST['storage_id'])
            try:
                storage = StorageRegistry.objects.get(id=storage_id)
                for k, v in request.POST['args']:
                    storage.storageargument_set.create(name=k, description=v.replace('&nbsp;', ' '))
                response['result'] = True
            except ObjectDoesNotExist:
                response['result'] = False
                response['message'] = u'添加失败：指定的存储过程不存在！'
        else:
            response['result'] = False
            response['message'] = illegal_error_message

        return HttpResponse(json.dumps(response))


@require_POST
def system_config_delete(request):
    pass


@require_http_methods(['GET', 'POST'])
def system_config_edit(request):
    pass


@require_GET
def system_config_detail(request, object_type, id):
    """
    根据对象类型和id获取详细信息
    """
    illegal_error_message = u'不合法的操作'
    response = {}
    obj = None

    if object_type not in ALLOWED_OBJECT_TYPES:
        response['result'] = False
        response['message'] = illegal_error_message
        return HttpResponse(response)

    if object_type == "1":
        """获取 ConnectionInfo 配置列表"""
        obj = ConnectionInfo
        title = '数据库连接'
        template_file = 'dbaux/connection_info_detail_tmpl.html'
        response['result'] = True
    elif object_type == "2":
        """获取 StorageRegistry 配置列表"""
        obj = StorageRegistry
        title = '存储过程'
        template_file = 'dbaux/storage_detail_tmpl.html'
        response['result'] = True
    else:
        response['result'] = False
        response['message'] = illegal_error_message

    if response['result']:
        item = obj.objects.get(id=id)
        content = {
            'title': title,
            'object_type': object_type,
            'id': id,
            'item': item,
        }
        t = loader.get_template(template_file)
        response['data'] = t.render(content, request)

    return HttpResponse(json.dumps(response))


@require_POST
def call_procedure(request):
    """
    操作执行接口，调用存储过程
    storage_id: 注册的存储过程ID
    args: 从前端页面获取的存储过程参数，dict类型
    """
    # operator = request.user.username
    storage_id = request.POST['storage_id']
    args = request.POST['args']
    response = dbhelper.call_procedure(storage_id=storage_id, args=args)

    return HttpResponse(response)


@require_POST
def get_procedure_by_connection_info_id(request):
    """获取指定数据库的所有存储过程"""
    # operator = request.user.username
    response = {}
    try:
        connection_info_id = request.POST['connection_info_id']
        response['result'] = True
        response['data'] = dbhelper.get_procedure_by_connection_info_id(connection_info_id)
    except ValueError:
        response['result'] = False
    return HttpResponse(json.dumps(response))


@require_POST
def get_procedure_arguments_by_storage_id(request):
    """获存储过程中定义的参数"""
    # operator = request.user.username
    pass
