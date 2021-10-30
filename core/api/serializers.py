from rest_framework import serializers
from core.models import PontoTuristico
from enderecos.api.serializers import EnderecoSerializer
from atracoes.api.serializers import AtracaoSerializer


class PontoTuristicoSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()
    atracoes = AtracaoSerializer(many=True)

    class Meta:
        model = PontoTuristico
        fields = ['id', 'nome', 'descricao', 'endereco', 'atracoes', 'foto']
