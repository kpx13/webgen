# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField
import pytils

class Article(models.Model):
    name = models.CharField(max_length=128, verbose_name=u'название')
    date = models.DateField(verbose_name=u'дата')
    text = RichTextField(verbose_name=u'текст')
    desc = models.TextField(max_length=512, verbose_name=u'сокращенный текст')
    slug = models.SlugField(verbose_name=u'slug', unique=True, blank=True, help_text=u'Заполнять не нужно')
    image = models.ImageField(upload_to='uploads/items', max_length=256, blank=True, verbose_name=u'изображение')
    order = models.SmallIntegerField(blank=True, default=0, verbose_name=u'порядок')
    show = models.BooleanField(verbose_name=u'показывать на сайте', default=False, blank=True)
   
    class Meta:
        verbose_name = u'статья'
        verbose_name_plural = u'статьи'
        ordering = ['-order']
    
    def __unicode__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=pytils.translit.slugify(self.name)
        super(Article, self).save(*args, **kwargs)
