from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auta/', views.AutoListView, name='AutoListView'),
    path('majitele/', views.MajitelListView, name='MajitelListView'),
]