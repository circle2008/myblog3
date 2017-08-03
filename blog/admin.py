#-*- coding: UTF-8 -*-
from django.contrib import admin
from models import Article
#引入数据模型，注册数据模型
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','content','pub_time')
    list_filter = ('pub_time',)
admin.site.register(Article,ArticleAdmin)