from django.urls import path

from .views import StudentAPIView


urlpatterns = [
    path('our-students/', StudentAPIView.as_view(), name='students')
]