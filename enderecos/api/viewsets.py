from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from enderecos.models import Endereco
from .serializers import EnderecoSerializer


class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    filter_backends = (SearchFilter, )
    search_fields = ['endereco_1', 'cidade', 'estado', 'pais']

