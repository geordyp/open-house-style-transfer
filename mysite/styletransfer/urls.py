from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView, name='views.index'),
    path('form/', views.FormView, name='views.form'),
    path('result/', views.ResultView, name='views.result'),
]
