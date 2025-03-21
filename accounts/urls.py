from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import UserRegistrationViewSet, UserLoginViewSet, UserCourseViewSet, UserProfileViewSet

router = DefaultRouter()
router.register('registration', UserRegistrationViewSet, basename="sign-user-up")
router.register('login', UserLoginViewSet, basename='log-user-in')
router.register('user/courses', UserCourseViewSet, basename='user-courses')
router.register('user/profile', UserProfileViewSet, basename='user-profile')

urlpatterns = [
    path('', include(router.urls)),
]
