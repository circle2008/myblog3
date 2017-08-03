#-*- coding: UTF-8 -*-
from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    articles=models.Article.objects.all()
    return render(request,'blog/index.html',{'articles':articles})

def article_page(request,article_id):
    articles = models.Article.objects.all()
    article=models.Article.objects.get(pk=article_id)
    return render(request,'blog/article_page.html',{'article':article,'articles':articles})

def edit_page(request,article_id):
    if article_id=='0':
        return render(request,'blog/edit_page.html')
    article=models.Article.objects.get(pk=article_id)
    return render(request,'blog/edit_page.html',{'article':article})
def edit_action(request):
    id=request.POST.get('article_id','0')
    title=request.POST.get('title','title')
    content=request.POST.get('content','content')
    if id=='0':
        models.Article.objects.create(title=title,content=content)
    else:
        article=models.Article.objects.get(pk=id)
        article.title=title
        article.content=content
        article.save()
    articles=models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})