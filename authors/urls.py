from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^authors/', views.authors, name='authors'),

    url(r'^author/(?P<pk>[0-9]+)/$', views.author_edit, name="author_edit"),


    url(r'^tag/', views.tag, name='tag'),

    ]