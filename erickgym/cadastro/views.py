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

    def get_queryset(self):
        usuario = self.request.user
        return Aluno.objects.filter(usuario=usuario)

    def post(self, request):
        request.data['usuario'] = request.user.pk
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class DetailUpdateDeleteAlunosView(RetrieveUpdateDestroyAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

    def put(self, request, pk, *args, **kwargs):
        user = request.user
        aluno = Aluno.objects.get(pk=pk)

        if aluno.usuario != user:
            return Response(
                {'detail': 'Você só pode editar seu próprio perfil'},
                status=400
            )

        return self.update(request, *args, **kwargs)
