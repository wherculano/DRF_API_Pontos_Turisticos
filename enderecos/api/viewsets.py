from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from enderecos.models import Endereco
from .serializers import EnderecoSerializer


class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )
    filter_backends = (SearchFilter, )
    search_fields = ['endereco_1', 'cidade', 'estado', 'pais']
    # lookup_field = 'nome'
    # altera o item padrão de busca (pk). O campo escolhido deverá ser unico no banco para manter a integridade do BD.
    # Pois não é possivel retornar mais de um dado. Assim, ao inves de usar o endpoint/pk/ pode-ser usar
    # endpoint/item_definido_no_lookup/
