from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.account),
    path('accounts/', views.account),
    path('auth/', views.auth,name='auth'),
    path('payment/', views.payment,name='payment'),
    path('accounts/login', views.login)
]