import django.http
from django.urls import path
from . import views
from django.views.generic.base import RedirectView
app_name = 'Tarot'
urlpatterns = [
    path('', views.TarotView.as_view(), name='home'),
]
