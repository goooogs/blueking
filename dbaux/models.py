# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class ConnectionInfo(models.Model):
    """数据库连接信息"""
    name = models.CharField(u'名称', max_length=30, unique=True, null=False)
    host = models.CharField(u'数据库主机', max_length=15)
    port = models.IntegerField(u'端口', default=3306)
    user = models.CharField(u'用户名', max_length=30)
    password = models.CharField(u'密码', max_length=40)
    database = models.CharField(u'数据库', max_length=20)
    charset = models.CharField(u'连接字符集', max_length=20, default='utf8')


class StorageRegistry(models.Model):
    """存储过程注册信息"""
    name = models.CharField(u'名称', max_length=30, unique=True, null=False)
    description = models.CharField(u'描述')
    storage_name = models.CharField(u'存储过程名称', max_length=100)
    input_arguments = models.CharField(u'参数', max_length=100)


class History(models.Model):
    '''操作历史'''
    login_user = models.CharField(u'操作用户', max_length=30)
    connection_info = models.CharField(u'连接信息', max_length=300)
    detail = models.CharField(u'操作内容', max_length=300)
    time = models.DateTimeField(u'时间', auto_now=True)

