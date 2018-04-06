from django.urls import path

from . import views

urlpatterns = [
    path('', views.indexView, name='views.index'),
    path('form/', views.formView, name='views.form'),
    path('result/', views.resultView, name='views.result'),
]
