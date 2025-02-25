from rest_framework import serializers
from app.models import Personaje, Arma

class PersonajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personaje
        fields = '__all__'

class ArmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arma
        fields = '__all__'