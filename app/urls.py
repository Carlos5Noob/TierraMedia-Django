from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from app import views

# paths de la aplicación

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
    path('combate/', views.pre_combate, name='lucha'),
    path("combate/<int:combate_id>/", views.combate, name="combate"),
    path("taberna/", views.taberna, name='taberna'),
    path('taberna/hablar/', views.hablar_npc, name='hablar_npc'),
    path('taberna/dados/', views.dados, name='dados'),
    path('crear_personaje/', views.crear_personaje, name='crear_personaje'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
