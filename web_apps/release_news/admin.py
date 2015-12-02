# Register your models here.
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from web_apps.release_news.models import Page


# 该类的作用当做一个装饰类来使用
class PageModelAdmin(SummernoteModelAdmin):
    pass


# 注册其他类的时候可以使用SomeModelAdmin
admin.site.register(Page, PageModelAdmin)
