from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import MyUser, Courses
from .serializers import CustomUserSerializer, CustomUserLoginSerializer, CustomUserProfileSerializer


"""Ro'yxatdan o'tish"""
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
    

"""Tizimga kirgizish"""
class UserLoginViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = CustomUserLoginSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    

"""User course-ga yozilishi va chiqishi"""
class UserCourseViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'slug'

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def join_to_course(self, request, *args, **kwargs):
        user = request.user
        course = self.get_object() 
        
        if course not in user.courses.all():
            user.courses.add(course)
            return Response({'message': "Siz kurs-ga muvaffaqiyatli yozildingiz."}, status=status.HTTP_200_OK)
        return Response({'message': "Siz allaqachon bu kurs-ga yozilgansiz."})
    
    @action(detail=True, methods=['delete'], permission_classes=[permissions.IsAuthenticated])
    def delete_course(self, request, *args, **kwargs):
        user = request.user
        course = self.get_object() 

        if course in user.courses.all():
            user.courses.remove(course)
            return Response({'message': f"Siz {course.name} nomli kurs-ni tark etdingiz."}, status=status.HTTP_200_OK)
        return Response({'message': f"Siz {course.name} nomli kurs-ga yozilmagansiz."})


    
"""User Profile"""
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = CustomUserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MyUser.objects.filter(id=self.request.user.id)
    
    def create(self, request, *args, **kwargs):
        return Response({'error': "POST amaliga ruhsat berilmagan."}, status=400)
    