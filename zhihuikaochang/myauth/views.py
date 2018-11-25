from django.shortcuts import render
from .models import User
from .serializers import UserRegisterSerializer, UserLoginSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class UserLoginApi(APIView):
    queryset = User.objects.all()

    def get(self, request):
        data = request.data
        if data.get('uid'):
            user = User.objects.filter(uid=data.get('uid'))
            serializer = UserLoginSerializer(user)
            return Response(serializer.data,status=status.HTTP_200_OK)
        serializer = UserLoginSerializer(self.__class__.queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self,request):
        data = request.data
        uid = data.get('uid')
        password = data.get('password')

        user = User.objects.get(uid=uid)
        if
