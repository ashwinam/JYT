from django.urls import path
from . import views

urlpatterns = [
    path('post_comment', views.post_comment, name='post_comment'),
    path('', views.blogHome, name='blogHome'),
    path('<str:slug>', views.blogPost, name='blogPost'),
]