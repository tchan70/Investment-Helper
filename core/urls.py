from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('compare-stocks/', views.compare_stocks, name='compare-stocks'),
]
