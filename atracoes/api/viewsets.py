from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from core.models import Atracao
from .serializers import AtracaoSerializer


class AtracaoViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    filter_fields = ['nome', 'descricao']
    filter_backends = (SearchFilter,)
    search_fields = ['nome', 'horario_func', 'idade_minima']
