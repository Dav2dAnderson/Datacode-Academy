from rest_framework import serializers

from django.contrib.auth.models import User

from .models import Course, Teacher, Student


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Student.objects.create(user=user)


class StudentSerializer(serializers.ModelSerializer):
    user_firstname = serializers.CharField(source="user.first_name", read_only=True)
    user_lastname = serializers.CharField(source='user.lastname', read_only=True)
    class Meta:
        model = Student
        fields = ['id', 'user', 'user_firstname', 'user_lastname','birth_date', 'courses']




