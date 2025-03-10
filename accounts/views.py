from rest_framework import viewsets, status, permissions
from rest_framework.response import Response

from .models import MyUser
from .serializers import CustomUserSerializer, CustomUserLoginSerializer


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
    

class UserLoginViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = CustomUserLoginSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    




    

