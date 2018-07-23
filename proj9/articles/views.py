from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

def articles(request):
     articles = Article.objects.all().order_by('date')
     return render(request, 'articles/index.html',{"articles": articles})

def single_article(request, slug):
     article = Article.objects.get(slug=slug)
     return render(request, 'articles/single.html',{"article": article})
     # return HttpResponse(slug)

@login_required(login_url='/accounts/login/')
def create(request):
     if request.method == 'POST':
          form = forms.CreateArticle(request.POST, request.FILES)
          if form.is_valid():
               #save to db
               return redirect('list')
     else:
          form = forms.CreateArticle()
     return render(request, 'articles/create.html', {'form': form})