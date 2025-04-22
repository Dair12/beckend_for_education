from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.contrib.auth.hashers import check_password
from .models import User
from .serializers import UserSerializer, LoginSerializer, RegisterSerializer, UserStatisticsSerializer
from user_tests.models import UserTest
from answers.models import UserAnswer

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            try:
                user = User.objects.get(email=email)
                if check_password(password, user.password_hash):
                    return Response({
                        'message': 'Login successful',
                        'user_id': user.id,
                        'role': user.role
                    }, status=status.HTTP_200_OK)
                return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
            except User.DoesNotExist:
                return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'message': 'Registration successful',
                'user_id': user.id
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        # Частичное обновление
        response = self.partial_update(request, *args, **kwargs)
        return Response({
            'message': f'User {self.kwargs["id"]} updated successfully'
        }, status=status.HTTP_200_OK)

class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        response = self.destroy(request, *args, **kwargs)
        return Response({
            'message': f'User {self.kwargs["id"]} deleted successfully'
        }, status=status.HTTP_200_OK)

class UserStatisticsView(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            tests_completed = UserTest.objects.filter(user_id=user_id, completed_at__isnull=False).count()
            correct_answers = UserAnswer.objects.filter(user_id=user_id, is_correct=True).count()
            serializer = UserStatisticsSerializer({
                'user_id': user_id,
                'tests_completed': tests_completed,
                'correct_answers': correct_answers
            })
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)