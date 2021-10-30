from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    filter_fields = ['id', 'nome', 'descricao', 'aprovado']
    filter_backends = (SearchFilter,)
    search_fields = ('nome', 'descricao', 'endereco__endereco_1')
    # 'endereco__endereco_1' Busca pelo campo endereco_1 no model/class Endereco, já que é um FK de PontoTuristico
