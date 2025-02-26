from rest_framework import serializers
from app.models import Personaje, Arma, Faccion, Ubicacion

class PersonajeSerializer(serializers.ModelSerializer):

    arma = serializers.StringRelatedField()  # Para mostrar el nombre del arma
    faccion = serializers.StringRelatedField()  # Para mostrar la facción
    ubicacion = serializers.StringRelatedField()  # Para mostrar la ubicación

    # Utilizamos String related field para mostar los nombres de las armas, facciones y ubicaciones en lugar de sus ids

    class Meta:
        model = Personaje
        fields = ['id', 'nombre', 'salud', 'victorias', 'derrotas', 'mana', 'arma', 'faccion', 'ubicacion', 'foto']

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