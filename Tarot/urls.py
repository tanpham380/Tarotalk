import django.http
from django.urls import path
from . import views
from django.views.generic.base import RedirectView


app_name = "Tarot"
urlpatterns = [

    path('', views.ViewUser.as_view(), name='HomePage'),
    path('login/', views.LoginPageView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.LogoutView, name='logout'),
    path('testpage/',  views.TestPageView.as_view(), name='HomePage'),
    path("chatbot/", views.TarotView.chatbot, name="chatbot"),
    path("list/", views.TarotView.listReader, name="list"),
    path("profile/", views.TarotView.profile, name="profile"),
    path("questions/", views.TarotView.question, name="questions"),
    path("package/", views.TarotView.package, name="package"),
    path("hour/", views.TarotView.hour, name="hour"),
    path("calendar/choose/", views.TarotView.chooseSlot, name="choose"),
    path("calendar/choose/checkout/", views.TarotView.checkout, name="checkout"),
    path("calendar/", views.TarotView.calendar, name="calendar"),
]