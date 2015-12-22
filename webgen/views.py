# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib import messages
from django.core.context_processors import csrf
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
import pytils

from request.forms import RequestForm
from pages.models import Page
from portfolio.models import Work
from blog.models import Article

def get_common_context(request):
    c = {}
    c['request_url'] = request.path
    c['works_r'] = Work.objects.filter(show=True)[:4]
    c['articles_r'] = Article.objects.filter(show=True)
    c['is_debug'] = settings.DEBUG
    c.update(csrf(request))
    return c

def page(request, page_name):
    c = get_common_context(request)
    c['page'] = get_object_or_404(Page, slug=page_name)
    return render_to_response('page.html', c, context_instance=RequestContext(request))

def home_page(request):
    c = get_common_context(request)
    c['request_url'] = 'home'
    c['page'] = get_object_or_404(Page, slug='home')
    return render_to_response('home.html', c, context_instance=RequestContext(request))

def portfolio_page(request, curr_work=None):
    c = get_common_context(request)
    if curr_work:
        c['curr_work'] = get_object_or_404(Work, slug=curr_work)
        return render_to_response('portfolio_work.html', c, context_instance=RequestContext(request))
    else:
        c['works'] = Work.objects.filter(show=False)
        return render_to_response('portfolio.html', c, context_instance=RequestContext(request))

def works(request):
    c = get_common_context(request)
    c['works'] = Work.objects.filter(show=True)
    return render_to_response('works.html', c, context_instance=RequestContext(request))

def articles_page(request, curr_work=None):
    c = get_common_context(request)
    if curr_work:
        c['curr_article'] = get_object_or_404(Article, slug=curr_work)
        return render_to_response('article.html', c, context_instance=RequestContext(request))
    else:
        c['articles'] = Article.objects.filter(show=True)
        return render_to_response('articles.html', c, context_instance=RequestContext(request))

def order_page(request):
    c = get_common_context(request)
    if request.method == 'GET':
        c['request_form'] = RequestForm()
    else:
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            if u'Клиентские базы' not in data['name']:
                message= u'Имя: ' + data['name'] + u"\n" + u'email: ' + data['email'] + '\n' + u'Телефон: ' + data['phone'] + '\n' + u'Текст: ' + data['comment'] + '\n'
                email = EmailMessage(u'Новое сообщение с сайта', message, settings.EMAIL_HOST_USER, settings.REQUEST_SEND_TO)
                file = request.FILES.get('brief')
                if file:
                    email.attach_file(handle_file(file))
                email.send()

            messages.success(request, u'Ваш запрос отправлен.')
            return HttpResponseRedirect('/')
        else:
            c['request_form'] = form
            messages.error(request, u'При обработке формы произошла ошибка.')
    c['page'] = get_object_or_404(Page, slug='order')
    return render_to_response('request.html', c, context_instance=RequestContext(request))


def about_page(request):
    c = get_common_context(request)
    c['page'] = get_object_or_404(Page, slug='about')
    return render_to_response('about.html', c, context_instance=RequestContext(request))

def contacts_page(request):
    c = get_common_context(request)
    c['page'] = get_object_or_404(Page, slug='contacts')
    return render_to_response('contacts.html', c, context_instance=RequestContext(request))

def umi_page(request):
    c = get_common_context(request)
    c['page'] = get_object_or_404(Page, slug='umi')
    return render_to_response('umi.html', c, context_instance=RequestContext(request))
    
def handle_file(f):
    filename = settings.ROOT_FOR_ATTACES + pytils.translit.translify(f.name)
    destination = open(filename, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
    return filename
