from rest_framework import serializers
from app.models import Personaje, Arma, Faccion, Ubicacion

class PersonajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personaje
        fields = '__all__'

class ArmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arma
        fields = '__all__'

class FaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faccion
        fields = '__all__'

class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = '__all__'