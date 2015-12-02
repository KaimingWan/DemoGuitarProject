# Create your models here.


# Page类在models.py中的定义
from django.db import models


class Category(models.Model):  # 发表的文章可以进行分类，要放在Page类前面
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'

    def __str__(self):
        return self.name


class Page(models.Model):
    title = models.CharField(u'标题', max_length=256)
    content = models.TextField(u'内容')
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)
    category = models.ForeignKey(Category)  # ForeignKey, 创建1对多关系的字段类型.
    url = models.URLField()
    views = models.IntegerField(default=0)

    class Meta:
        verbose_name = '文章'  # 后台显示的名字
        verbose_name_plural = '文章'  # 后台显示的名字的复数

    def __str__(self):
        return self.title  # 按照标题来显示每个实例，也就是一行数据
