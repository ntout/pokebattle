from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions
from .serializers import MyTokenObtainPairSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

class ObtainTokenPair(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserCreate(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)




class HelloWorldView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(data={'hello':'world'}, status=status.HTTP_200_OK)