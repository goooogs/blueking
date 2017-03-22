# -*- coding: utf-8 -*-

from django.db import models


'''
知乎问题
'''
class Question(models.Model):
    id = models.IntegerField(u'问题ID', primary_key=True)
    title = models.CharField(u'标题', max_length=100)



'''
热门回复
'''
class Answer(models.Model):
    id = models.IntegerField(u'回帖ID', primary_key=True)
    vote_count = models.IntegerField(u'票数', default=0)
    author = models.CharField(u'回帖人', max_length=30)
    bio = models.CharField(u'回帖人说明', max_length=100, default=None)
    summary = models.TextField(u'摘要', max_length=300)
    href = models.CharField(u'href', max_length=1024)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

