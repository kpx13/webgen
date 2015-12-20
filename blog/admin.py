# -*- coding: utf-8 -*-
from django.contrib import admin
import models

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'text', 'order', 'show')
    search_fields = ('name', 'text')
    ordering = ('date', )

admin.site.register(models.Article, ArticleAdmin)