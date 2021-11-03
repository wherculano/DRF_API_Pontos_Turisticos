from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated  # IsAdminUser (permite que somente ADM tenha acesso)
from rest_framework.viewsets import ModelViewSet

from comentarios.models import Comentario
from .serializers import ComentarioSerializer


class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )

    filter_fields = ['usuario', 'data', 'aprovado']
    filter_backends = (SearchFilter, )
    search_fields = ['usuario', 'data', 'aprovado']
