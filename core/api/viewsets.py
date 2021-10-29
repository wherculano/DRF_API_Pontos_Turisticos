from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    filter_fields = ['id', 'nome', 'descricao', 'aprovado']

    # @action(methods=['POST'], detail=True)  # Action Personalizada. Detail True disponibiliza a PK
    # def denunciar(self, request, pk=None):  # acessa um recurso (pk) em especifico
    #     """Efetua denuncia de um ponto turistico (pontosturisticos/id/denunciar)"""
    #     pass
    #
    # @action(methods=['GET'], detail=False)
    # def teste(self, request):  # acessa o endpoint como um todo
    #     pass
