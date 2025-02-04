from django.urls import path, include
from app import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('personajes/', views.ListCharacters.as_view(), name='personajes'),
    path('armas/', views.ListWeapons.as_view(), name='armas'),
    path('ubicacion/', views.Ubicaciones.as_view(), name='ubicacion'),
]
