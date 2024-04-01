from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from treinos.models import Exercicio
from treinos.serializers import ExercicioSerializer


# CBV - Class-Based View

class ListCreateExerciciosView(APIView):

    def get(self, request):
        exercicios = Exercicio.objects.all()
        serializer = ExercicioSerializer(exercicios, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        #  pegar os dados do request e criar um novo exercicios
        serializer = ExercicioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


class DetailUpdateDeleteExerciciosView(APIView):

    def get_object(self, pk):
        try:
            exercicio = Exercicio.objects.get(pk=pk)
            return exercicio
        except Exercicio.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        exercicio = self.get_object(pk)
        serializer = ExercicioSerializer(instance=exercicio)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        exercicio = self.get_object(pk)
        exercicio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        exercicio = self.get_object(pk)
        serializer = ExercicioSerializer(instance=exercicio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
