from rest_framework.serializers import ModelSerializer, ValidationError
from core.models import Cidade, Estado


class CidadeSerializer(ModelSerializer):
    class Meta:
        model = Cidade
        fields = ['nome']

    def validade_nome(self, value):
        if len(value) < 3:
            raise ValidationError(
                detail='Não é permitido cidade com menos de 3 letras')
        return value

    def validate(self, data):
        # data[atributo]

        return data


class EstadoSerializer(ModelSerializer):
    class Meta:
        mode = Estado
        fields = ['sigla', 'nome']
