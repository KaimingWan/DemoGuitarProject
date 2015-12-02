from django.apps import AppConfig

__author__ = 'Kami Wan'


# 对models类设置一个对应的配置类，用于显示别名。需要在app的__init__.py中启用该配置
class PageConfig(AppConfig):
    name = 'web_apps.release_news'
    verbose_name = '发布新闻'  # 在后台显示的app名字使用该名字
