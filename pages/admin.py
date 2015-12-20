# -*- coding: utf-8 -*-
from django.contrib import admin
import models

class PageAdmin(admin.ModelAdmin):
	list_display = ('slug', 'title', 'subintro_title')
	search_fields = ('title', 'content')

admin.site.register(models.Page, PageAdmin)
