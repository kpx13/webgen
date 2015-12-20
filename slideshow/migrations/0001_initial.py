# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-20 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(max_length=256, upload_to=b'slider', verbose_name='\u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0430')),
                ('title', models.CharField(blank=True, max_length=256, verbose_name='\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('subtitle', models.CharField(blank=True, max_length=256, verbose_name='\u043f\u043e\u0434\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('description', models.CharField(max_length=1024, verbose_name='\u0442\u0435\u043a\u0441\u0442')),
                ('link', models.CharField(blank=True, help_text='\u0421\u0441\u044b\u043b\u043a\u0430 \u0441\u043d\u0438\u0437\u0443, \u0435\u0441\u043b\u0438 \u0435\u0441\u0442\u044c', max_length=256, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430')),
                ('show', models.BooleanField(default=True, help_text='\u041e\u0442\u043c\u0435\u0442\u044c\u0442\u0435 \u0433\u0430\u043b\u043e\u0447\u043a\u043e\u0439, \u0447\u0442\u043e\u0431\u044b \u043f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u044d\u0442\u043e\u0442 \u0441\u043b\u0430\u0439\u0434', verbose_name='\u043f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u043d\u0430 \u0441\u0430\u0439\u0442\u0435?')),
                ('sort_parameter', models.IntegerField(blank=True, default=0, help_text='\u2116 \u0441\u043b\u0430\u0439\u0434\u0435\u0440\u0430: 1\u0439, 2\u0439 \u0438\u043b\u0438 3\u0439', verbose_name='\u043f\u043e\u0440\u044f\u0434\u043e\u043a \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438')),
            ],
            options={
                'ordering': ['sort_parameter'],
                'verbose_name': '\u0441\u043b\u0430\u0439\u0434\u0435\u0440',
                'verbose_name_plural': '\u0441\u043b\u0430\u0439\u0434\u0435\u0440',
            },
        ),
    ]