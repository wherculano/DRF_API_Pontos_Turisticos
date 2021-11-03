from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)  # permite apenas leitura se nao estiver autenticado
    authentication_classes = (TokenAuthentication,)
    filter_fields = ['id', 'nome', 'descricao', 'aprovado']
    filter_backends = (SearchFilter,)
    search_fields = ('nome', 'descricao', 'endereco__endereco_1')
    # 'endereco__endereco_1' Busca pelo campo endereco_1 no model/class Endereco, já que é um FK de PontoTuristico

    # IsAdminUser (permite que somente ADM tenha acesso)
    # DjangoModelPermission dará acesso a apenas as permissões que estiverem 'setadas' no DjangoAdmin
    # Para cada Model o admin gera 3 permissões padrões: add, change, del (que precisam ser adicionadas a cada user)
