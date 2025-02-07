from django.urls import path, include
from app import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('personajes/', views.ListCharacters.as_view(), name='personajes'),
    path('armas/', views.ListWeapons.as_view(), name='armas'),
    path('facciones/', views.ListFactions.as_view(), name='facciones'),
    path('ubicaciones/', views.Ubicaciones.as_view(), name='ubicaciones'),
    path('personajes/<int:pk>/', views.DetailCharacters.as_view(), name='personajes_id'),
    path('armas/<int:pk>/', views.DetailArma.as_view(), name='armas_id'),
    path('facciones/<int:pk>/', views.DetailFaccion.as_view(), name='facciones_id'),
    path('ubicaciones/<int:pk>/', views.DetailUbicacion.as_view(), name='ubicaciones_id'),
]
