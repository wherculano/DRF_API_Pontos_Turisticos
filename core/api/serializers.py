from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from atracoes.api.serializers import AtracaoSerializer
from core.models import PontoTuristico, Atracao
from enderecos.api.serializers import EnderecoSerializer


class PontoTuristicoSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()
    atracoes = AtracaoSerializer(many=True)
    descricao_completa = SerializerMethodField(read_only=True)

    class Meta:
        model = PontoTuristico
        fields = ['id', 'nome', 'descricao', 'endereco', 'atracoes', 'foto', 'descricao_completa']
        read_only_fields = ('comentarios', 'avaliacoes')

    @staticmethod
    def get_descricao_completa(obj):
        return f'{obj.nome}: {obj.descricao}'

    # -- Criando Relação Many To Many --
    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']
        ponto = PontoTuristico.objects.create(**validated_data)
        self.create_atracoes(atracoes, ponto)

        return ponto

    @staticmethod
    def create_atracoes(atracoes, ponto):
        for atracao in atracoes:
            atrac = Atracao.objects.create(**atracao)
            ponto.attrcoes.add(atrac)
