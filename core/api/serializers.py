from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from atracoes.api.serializers import AtracaoSerializer
from core.models import PontoTuristico, DocIdentificacao
from enderecos.api.serializers import EnderecoSerializer
from atracoes.models import Atracao
from enderecos.models import Endereco


class DocIdentificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocIdentificacao
        fields = '__all__'


class PontoTuristicoSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()
    atracoes = AtracaoSerializer(many=True)
    descricao_completa = SerializerMethodField(read_only=True)
    doc_identificacao = DocIdentificacaoSerializer()

    class Meta:
        model = PontoTuristico
        fields = ['id', 'nome', 'descricao', 'endereco', 'atracoes', 'foto', 'descricao_completa', 'doc_identificacao']
        read_only_fields = ('comentarios', 'avaliacoes')

    @staticmethod
    def get_descricao_completa(obj):
        return f'{obj.nome}: {obj.descricao}'

    def create(self, validated_data):
        # -- Relação Many To Many --
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']

        # -- Foreign Key relationship --
        endereco = validated_data['endereco']
        del validated_data['endereco']
        end = Endereco.objects.create(**endereco)

        # OneToOne relationship
        doc = validated_data['doc_identificacao']
        del validated_data['doc_identificacao']
        doc_ident = DocIdentificacao.objects.create(**doc)

        ponto = PontoTuristico.objects.create(**validated_data)

        self.create_atracoes(atracoes, ponto)
        ponto.endereco = end
        ponto.doc_identificacao = doc_ident
        ponto.save()

        return ponto

    @staticmethod
    def create_atracoes(atracoes, ponto):
        # -- Relação Many To Many --
        for atracao in atracoes:
            atrac = Atracao.objects.create(**atracao)
            ponto.attrcoes.add(atrac)
