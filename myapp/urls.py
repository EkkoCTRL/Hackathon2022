from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('disaster/', views.disaster),
    path('content/', views.content),

]
