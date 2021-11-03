from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from avaliacoes.models import Avaliacao
from .serializers import AvaliacaoSerializer


class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    filter_fields = ['usuario', 'nota', 'data']
    filter_backends = (SearchFilter, )
    search_fields = ['nota', 'data']
