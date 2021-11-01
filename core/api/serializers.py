from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from core.models import PontoTuristico
from enderecos.api.serializers import EnderecoSerializer
from atracoes.api.serializers import AtracaoSerializer


class PontoTuristicoSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()
    atracoes = AtracaoSerializer(many=True)
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ['id', 'nome', 'descricao', 'endereco', 'atracoes', 'foto', 'descricao_completa']

    @staticmethod
    def get_descricao_completa(obj):
        return f'{obj.nome}: {obj.descricao}'
