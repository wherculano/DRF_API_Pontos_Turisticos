from rest_framework.serializers import ModelSerializer
from comentarios.models import Comentario


class ComentarioSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['id', 'usuario', 'comentario', 'data', 'aprovado']

    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     rep['usuario'] = UserSerializer(instance.usuario).data  # ToDo ver como criar serializer do User