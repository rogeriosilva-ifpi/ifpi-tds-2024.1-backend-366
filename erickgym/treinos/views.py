from rest_framework.views import APIView
from rest_framework.response import Response
from treinos.models import Exercicio
from treinos.serializers import ExercicioSerializer


# CBV - Class-Based View
class ListaExerciciosView(APIView):

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
