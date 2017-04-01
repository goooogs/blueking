# -*- coding: utf-8 -*-
import pymysql.cursors

from .models import ConnectionInfo, StorageRegistry


def call_procedure(storage_id, args=None):
    """
    @apiDescription 调用存储过程
    @apiParam {int} storage_id 已注册的存储过程ID
    @apiParam {list} [args] 存储过程参数
    """
    storage = StorageRegistry.objects.get(id=storage_id)
    connection_info = storage.connection_info
    args = [v for v in args.itervalues()] if isinstance(args, dict) else None
    response = {}

    conn = pymysql.connect(db=connection_info.database,
                           user=connection_info.user,
                           password=connection_info.password,
                           host=connection_info.host,
                           port=connection_info.port,
                           charset=connection_info.charset,
                           cursorclass=pymysql.cursors.DictCursor)
    try:
        with conn.cursor() as cursor:
            if args:
                cursor.callproc('update_phone_number_by_uid', args)
            else:
                cursor.callproc('update_phone_number_by_uid')
            conn.commit()
            if cursor.rowcount == 1:
                response['result'] = True
                response['message'] = u'操作成功'
                response['row_count'] = 1
            else:
                response['result'] = False
                response['message'] = u'操作失败'
                response['row_count'] = cursor.rowcount
    finally:
        conn.close()
        response['result'] = False
        response['message'] = u'数据格式不正确'

    return response


def get_procedure_by_database(db):
    """获取指定数据库下的存储过程"""
    pass


def get_runction_by_database(db):
    """获取指定数据库下的函数"""
    pass



