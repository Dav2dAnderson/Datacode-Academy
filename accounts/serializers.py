from rest_framework import serializers

from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'phone', 'role', 'password', 'password_confirmation']
        extra_kwargs = {'password': {"write_only": True}}

    def validate_password(self, value):
        validate_password(value)
        return value
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirmation']:
            raise serializers.ValidationError({'password': "Parollar mos kelmadi."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        return User.objects.create_user(**validated_data)
        