from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Aluno
from .serializers import AlunoSerializer

"""
class ListCreateAlunoView(APIView):

    def get(self, request):
        alunos = Aluno.objects.all()
        serializer = AlunoSerializer(instance=alunos, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = AlunoSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
"""


class ListCreateAlunoView(ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class DetailUpdateDeleteAlunosView(RetrieveUpdateDestroyAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
