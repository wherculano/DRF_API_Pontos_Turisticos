from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from comentarios.models import Comentario
from .serializers import ComentarioSerializer


class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    filter_fields = ['usuario', 'data', 'aprovado']
    filter_backends = (SearchFilter, )
    search_fields = ['usuario', 'data', 'aprovado']
