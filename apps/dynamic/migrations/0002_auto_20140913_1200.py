# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rooms',
            options={'verbose_name': '\u041a\u043e\u043c\u043d\u0430\u0442\u044b', 'verbose_name_plural': '\u041a\u043e\u043c\u043d\u0430\u0442\u044b'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': '\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438', 'verbose_name_plural': '\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438'},
        ),
        migrations.AlterField(
            model_name='users',
            name='date_joined',
            field=models.DateField(default=datetime.datetime.now, verbose_name='\u0414\u0430\u0442\u0430 \u043f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f \u043d\u0430 \u0440\u0430\u0431\u043e\u0442\u0443'),
        ),
    ]
