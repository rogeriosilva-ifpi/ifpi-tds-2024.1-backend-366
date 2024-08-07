from django.shortcuts import render
<<<<<<< HEAD

# Create your views here.
=======
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from core.models import Estado
from core.serializers import EstadoSerializer


class ListCreateEstado(APIView):  # CBV: Class-Based View

    def get(self, request):
        estados = Estado.objects.all()
        serializer = EstadoSerializer(estados, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EstadoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        return Response(data, status=status.HTTP_201_CREATED)


class DetailUpdateDeleteEstado(RetrieveUpdateDestroyAPIView):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer


"""
Via APIView


class DetailUpdateDeleteEstado(APIView):

    def get(self, request, pk):
        pass

    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass
"""
>>>>>>> 6be5c1bc3f4c4c87de31d30b744723fedcabb4a9
