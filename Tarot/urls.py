import django.http
from django.urls import path
from . import views
from django.views.generic.base import RedirectView
app_name = 'Tarot'
urlpatterns = [
    path('', views.ViewUser.as_view(), name='HomePage'),
    path('login/', views.LoginPageView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.LogoutView, name='logout'),
    path('testpage/',  views.TestPageView.as_view(), name='HomePage'),
]
