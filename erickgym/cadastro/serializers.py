from rest_framework import serializers
from .models import Aluno
from autorizacao.serializers import UserSimpleSerializer


class AlunoSerializer(serializers.ModelSerializer):

    usuario = UserSimpleSerializer(read_only=True)

    class Meta:
        model = Aluno
        fields = '__all__'
