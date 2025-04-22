from rest_framework import serializers
from .models import UserTest, TestQuestion
from questions.serializers import QuestionSerializer
from users.models import User
from exams.models import Exam

class TestQuestionSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()

    class Meta:
        model = TestQuestion
        fields = ['id', 'question', 'question_order']

class UserTestSerializer(serializers.ModelSerializer):
    questions = TestQuestionSerializer(many=True, read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    exam = serializers.PrimaryKeyRelatedField(queryset=Exam.objects.all())

    class Meta:
        model = UserTest
        fields = ['id', 'user', 'exam', 'language_code', 'created_at', 'completed_at', 'questions']
        read_only_fields = ['id', 'created_at', 'completed_at']

class UserTestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTest
        fields = ['user', 'exam', 'language_code']