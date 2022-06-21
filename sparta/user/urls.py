from django.contrib import admin
from django.urls import path, include
from user import views

urlpatterns = [
    path('login/', views.UserAPIView.as_view()),
    path('logout/', views.UserAPIView.as_view()),
    path('info/', views.UserInfoView.as_view()),
    path('', views.UserView.as_view()),
]