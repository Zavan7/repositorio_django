from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('codeum/', views.cod1, name='codeum'),
    path('codedois/', views.cod2, name='codedois'),
    path('codetres/', views.cod3, name='codetres'),
]