# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.IntegerField(serialize=False, verbose_name='\u56de\u5e16ID', primary_key=True)),
                ('vote_count', models.IntegerField(default=0, verbose_name='\u7968\u6570')),
                ('author', models.CharField(max_length=30, verbose_name='\u56de\u5e16\u4eba')),
                ('bio', models.CharField(default=None, max_length=100, verbose_name='\u56de\u5e16\u4eba\u8bf4\u660e')),
                ('summary', models.TextField(max_length=300, verbose_name='\u6458\u8981')),
                ('href', models.CharField(max_length=1024, verbose_name='href')),
            ],
        ),
        migrations.CreateModel(
            name='CalcHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('multiplier', models.IntegerField(verbose_name='\u4e58\u6570')),
                ('multiplicand', models.IntegerField(verbose_name='\u88ab\u4e58\u6570')),
                ('calc_result', models.IntegerField(verbose_name='\u8ba1\u7b97\u7ed3\u679c')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.IntegerField(serialize=False, verbose_name='\u95ee\u9898ID', primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='home_application.Question'),
        ),
    ]
