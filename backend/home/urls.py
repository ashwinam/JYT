from django.urls import path
from . import views

urlpatterns= [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('signup/', views.signUpHandler, name='signUpHandler'),
    path('login/', views.loginHandler, name='loginHandler'),
    path('logout/', views.logoutHandler, name='logoutHandler'),
]