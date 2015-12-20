# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from filebrowser.sites import site
from django.conf.urls.static import static
admin.autodiscover()

import settings
import views

urlpatterns = [
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^admin/jsi18n/', 'django.views.i18n.javascript_catalog'),
    #url(r'^ckeditor/', include('ckeditor.urls')),

    url(r'^$' , views.home_page, name='home'),
    url(r'^order/$' , views.order_page, name='order'),
    url(r'^about/$' , views.about_page, name='about'),
    url(r'^contacts/$' , views.contacts_page, name='contacts'),
    url(r'^portfolio/$' , views.portfolio_page, name='portfolio'),
    url(r'^articles/$' , views.articles_page, name='articles'),
    url(r'^works/$' , views.works, name='works'),
    url(r'^portfolio/(?P<curr_work>[\w-]+)/$' , views.portfolio_page, name='work'),
    url(r'^articles/(?P<curr_work>[\w-]+)/$' , views.articles_page, name='article'),
    url(r'^(?P<page_name>[\w-]+)/$' , views.page, name='page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
