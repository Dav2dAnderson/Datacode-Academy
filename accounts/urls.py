from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import UserRegistrationViewSet



router = DefaultRouter()
router.register('registration', UserRegistrationViewSet, basename="sign-user-up")

urlpatterns = [
    path('', include(router.urls)),
]