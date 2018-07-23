# re_path(r'^(?P<slug>\w+)/$', views.single_article, name='single'),

from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
]