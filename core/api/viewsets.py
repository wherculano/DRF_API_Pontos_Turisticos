from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    http_method_names = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']  # lista de metodos que o endpoint aceitará

    def get_queryset(self):  # metodo que sobrescreve a variavel queryset
        return PontoTuristico.objects.filter(aprovado=True)

    def list(self, request, *args, **kwargs):  # sobrescreve a ação do GET do endpoint como um todo
        # Sobrescreveu o método, mas continua tendo o mesmo resultado caso este não tivesse sido implementado.
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):  # sobrescreve a ação do POST e retorna o que eu desejar
        # Os valores passados no POST sao pegos pelo request.data['chave']
        # Sobrescreveu o método, mas continua tendo o mesmo resultado caso este não tivesse sido implementado.
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):  # sobrescreve a ação do DELETE e retorna o que eu desejar
        # com o kwargs['pk'] posso pegar o ID passado na url e fazer os tratamentos necessários
        # Sobrescreveu o método, mas continua tendo o mesmo resultado caso este não tivesse sido implementado.
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):  # sobrescreve a ação do GET de um recurso (endpoint/item/)
        # Sobrescreveu o método, mas continua tendo o mesmo resultado caso este não tivesse sido implementado.
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):  # sobrescreve a ação do PUT
        # atraves do kwargs['pk'] acesso o item solicitado e pelo request.data['campo'] acesso os valores
        # Sobrescreveu o método, mas continua tendo o mesmo resultado caso este não tivesse sido implementado.
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):  # sobrescreve a ação do PATCH
        # Sobrescreveu o método, mas continua tendo o mesmo resultado caso este não tivesse sido implementado.
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    @action(methods=['POST'], detail=True)  # Action Personalizada. Detail True disponibiliza a PK
    def denunciar(self, request, pk=None):  # acessa um recurso (pk) em especifico
        """Efetua denuncia de um ponto turistico (pontosturisticos/id/denunciar)"""
        pass

    @action(methods=['GET'], detail=False)
    def teste(self, request):  # acessa o endpoint como um todo
        pass