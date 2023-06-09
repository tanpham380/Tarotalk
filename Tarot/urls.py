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
    path('testpage/',  views.TestPageView.as_view(), name='HomePagetesst'),
    path("profile/user/<int:user_id>/", views.profileuser.as_view(), name="profile"),
    path("questions/user/<int:user_id>/", views.question.as_view(), name="questions"),
    path("chatbot/", chatbot, name="chatbot"),
    path("package/user/<int:user_id>/", views.package.as_view(), name="package"),
    path("hour/user/<int:user_id>/", views.hour.as_view() , name="hour"),
    path("calendar/choose/", chooseSlot, name="choose"),
    path("calendar/choose/checkout/", views.checkout.as_view(), name="checkout"), 
    path("calendar/user/<int:user_id>/", views.calendar.as_view(), name="calendar"),
    path("guide/", views.GuideView.as_view(), name="guide"),
    path("account/", views.Account.as_view(), name="account"),
    path("event/", views.EventView.as_view(), name="event"),
    path("post/", views.PostView.as_view(), name="post"),
    path("morereader/", views.MoreReaderView.as_view(), name="morereader"),
    path("xinloi/", xinloipagenaychuahoatdong, name="xinloi"),
    path("paid/", views.PaidSuccessfullyView.as_view(), name="paid"),
    path("upgradeUser/", views.UpdateUserView.as_view(), name="upgradeUser"),
    #  path('user/<int:user_id>/', views.user_detail, name='user_detail'),
] 