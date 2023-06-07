import django.http
from django.urls import path
from . import views
from django.views.generic.base import RedirectView
from .views import *


app_name = "Tarot"
urlpatterns = [

    path('', views.ViewUser.as_view(), name='HomePage'),
    path('login/', views.LoginPageView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.LogoutView, name='logout'),
    path('testpage/',  views.TestPageView.as_view(), name='HomePage'),
    path("list/", listReader, name="list"),
    path("profile/", profile, name="profile"),
    path("questions/", question, name="questions"),
    path("chatbot/", chatbot, name="chatbot"),
    path("package/", package, name="package"),
    path("hour/", hour, name="hour"),
    path("calendar/choose/", chooseSlot, name="choose"),
    path("calendar/choose/checkout/", checkout, name="checkout"),
    path("calendar/", calendar, name="calendar"),
]