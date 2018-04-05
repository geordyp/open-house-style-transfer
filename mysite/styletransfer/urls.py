from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView, name='styletransfer.views.index'),
    path('form/', views.FormView, name='styletransfer.views.form'),
    path('result/', views.ResultView, name='styletransfer.views.result'),
]
