from django.shortcuts import render

from rest_framework import viewsets, status, permissions
from rest_framework.response import Response

from .models import MyUser
from .serializers import CustomUserSerializer
# Create your views here.


class UserRegistrationViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = CustomUserSerializer
    http_method_names = ['post']
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': "Foydalanuvchi muvaffaqiyatli yaratildi.", "user": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    




    

