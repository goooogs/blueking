# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calchistory',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u5df2\u5220\u9664'),
        ),
    ]
