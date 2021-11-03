from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from atracoes.api.serializers import AtracaoSerializer
from core.models import PontoTuristico
from enderecos.api.serializers import EnderecoSerializer
from atracoes.models import Atracao
from enderecos.models import Endereco


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

        # Foreign Key relationship
        endereco = validated_data['endereco']
        del validated_data['endereco']
        end = Endereco.objects.create(**endereco)
        ponto.endereco = end
        ponto.save()

        return ponto

    @staticmethod
    def create_atracoes(atracoes, ponto):
        # -- Relação Many To Many --
        for atracao in atracoes:
            atrac = Atracao.objects.create(**atracao)
            ponto.attrcoes.add(atrac)
