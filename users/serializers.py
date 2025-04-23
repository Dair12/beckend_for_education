from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'role', 'created_at']
        read_only_fields = ['id', 'created_at']

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'role']
        extra_kwargs = {'role': {'default': 'User'}}

    def create(self, validated_data):
        # Создание пользователя с хешированным паролем
        user = User(
            name=validated_data['name'],
            email=validated_data['email'],
            password_hash=validated_data['password'],
            role=validated_data.get('role', 'User')
        )
        user.save()
        return user

class AdminRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        extra_kwargs = {'role': {'default': 'Admin'}}

    def create(self, validated_data):
        # Создание администратора с хешированным паролем
        user = User(
            name=validated_data['name'],
            email=validated_data['email'],
            password_hash=validated_data['password'],
            role='Admin'
        )
        user.save()
        return user

class UserStatisticsSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    tests_completed = serializers.IntegerField()
    correct_answers = serializers.IntegerField()