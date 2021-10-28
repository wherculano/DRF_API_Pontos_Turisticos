from rest_framework import serializers
from enderecos.models import Endereco


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['id', 'endereco_1', 'cidade', 'estado', 'pais', 'latitude', 'longitude']
