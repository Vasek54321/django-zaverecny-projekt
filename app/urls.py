from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('auta/', views.AutoListView, name='AutoListView'),
    path('majitele/', views.MajitelListView, name='MajitelListView'),
    path('vyrobci/', views.VyrobceListView, name='VyrobceListView'),

    path('auto/<int:id_auto>/', views.AutoDetailView, name='AutoDetailView'),
    path('majitel/<int:id_majitel>/', views.MajitelDetailView, name='MajitelDetailView'),
    path('vyrobce/<int:id_vyrobce>/', views.VyrobceDetailView, name='VyrobceDetailView'),
]