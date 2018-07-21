from django.shortcuts import render
from .models import Articles

# Create your views here.
all_article_objects = Articles.objects.all().order_by('time')

def articles(request):
     return render(request, 'articles/articles.html',{'articles': all_article_objects})