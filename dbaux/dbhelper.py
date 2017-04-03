# -*- coding: utf-8 -*-
import pymysql.cursors

from .models import ConnectionInfo, StorageRegistry


def get_connection_by_connection_info_id(connection_info_id):
    """
    根据注册的数据库连接信息ID获取数据库连接对象
    :param connection_info_id: 已注册的数据库连接信息ID
    :return: 已打开的数据库连接对象
    """
    connection_info = ConnectionInfo.objects.get(id=connection_info_id)
    conn = pymysql.connect(db=connection_info.database,
                           user=connection_info.user,
                           password=connection_info.password,
                           host=connection_info.host,
                           port=connection_info.port,
                           charset=connection_info.charset,
                           cursorclass=pymysql.cursors.DictCursor)
    return conn


def get_connection_by_storage_id(storage_id):
    """
    根据注册的存储过程ID获取数据库连接对象
    :param storage_id: 已注册的存储过程ID
    :return: 已打开的数据库连接对象
    """
    storage = StorageRegistry.objects.get(id=storage_id)
    connection_info = storage.connection_info
    conn = pymysql.connect(db=connection_info.database,
                           user=connection_info.user,
                           password=connection_info.password,
                           host=connection_info.host,
                           port=connection_info.port,
                           charset=connection_info.charset,
                           cursorclass=pymysql.cursors.DictCursor)
    return conn


def call_procedure(storage_id, args=None):
    """
    调用存储过程
    :param storage_id: 已注册的存储过程ID
    :param args: 存储过程参数，dict类型
    :return: 标识操作是否成功的json数据
    """
    args = [v for v in args.itervalues()] if isinstance(args, dict) else None
    response = {}

    conn = get_connection_by_storage_id(storage_id=storage_id)

    try:
        with conn.cursor() as cursor:
            if args:
                cursor.callproc('update_phone_number_by_uid', args)
            else:
                cursor.callproc('update_phone_number_by_uid')
            conn.commit()
            if (args and cursor.rowcount == 1) or (not args and cursor.rowcount >= 1):
                # 带参数的只能影响一条记录，不带参数的至少影响一条记录
                response['result'] = True
                response['message'] = u'操作成功'
            else:
                response['result'] = False
                response['message'] = u'操作失败'
            response['row_count'] = cursor.rowcount
    finally:
        conn.close()

    return response


def get_procedure_by_connection_info_id(connection_info_id):
    """
    获取指定连接ID对应数据库中的所有存储过程
    :param connection_info_id: 已注册的数据库连接信息ID
    :return: 返回指定数据库中的所有存储过程名称
        Example:
        [u'storage_name_1', u'storage_name_2']
    """
    connection_info = ConnectionInfo.objects.get(id=connection_info_id)
    sql = "select name from mysql.proc where db=%s and type='procedure'"

    conn = get_connection_by_connection_info_id(connection_info_id)
    items = []

    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, connection_info.database)
            data_set = cursor.fetchall()
            items = [i['name'] for i in data_set]
    finally:
        conn.close()

    return items


def get_runction_by_connection_info_id(db):
    """获取指定数据库下的函数"""
    pass



