from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import action

from dj_rest_auth.registration.views import RegisterView

from .models import MyUser, Courses
from .serializers import CustomUserProfileSerializer
from .tasks import welcome_text_email


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
            notify_about_updates.delay(to=user.id, content=f"Siz {course} kursiga muvaffaqiyatli qo'shildingiz.")
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
    


