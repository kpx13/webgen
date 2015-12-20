# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.context_processors import csrf
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Page

def get_common_context(request):
    c = {}
    c['request_url'] = request.path
    c['is_debug'] = settings.DEBUG
    c.update(csrf(request))
    return c

def page(request, page_name):
    c = get_common_context(request)
    c['page'] = get_object_or_404(Page, slug=page_name)
    return render_to_response('page.html', c, context_instance=RequestContext(request))