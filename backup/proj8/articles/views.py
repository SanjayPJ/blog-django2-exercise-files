from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

# Create your views here.

def articles(request):
     articles = Article.objects.all().order_by('date')
     return render(request, 'articles/index.html',{"articles": articles})

def single_article(request, slug):
     article = Article.objects.get(slug=slug)
     return render(request, 'articles/single.html',{"article": article})
     # return HttpResponse(slug)