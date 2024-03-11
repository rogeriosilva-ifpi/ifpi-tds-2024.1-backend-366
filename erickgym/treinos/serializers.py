from rest_framework import serializers
from treinos.models import Exercicio


class ExercicioSerializer(serializers.ModelSerializer):
  class Meta:
    model = Exercicio
    fields = '__all__'