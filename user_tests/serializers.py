from rest_framework import serializers
from .models import UserTest, TestQuestion
from questions.serializers import QuestionSerializer
from users.serializers import UserSerializer
from exams.serializers import ExamSerializer

class TestQuestionSerializer(serializers.ModelSerializer):
    variant_question = QuestionSerializer()

    class Meta:
        model = TestQuestion
        fields = ['id', 'variant_question', 'question_order']

class UserTestSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    exam = ExamSerializer(read_only=True)
    test_questions = TestQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = UserTest
        fields = ['id', 'user', 'exam', 'language_code', 'created_at', 'completed_at', 'test_questions']

class UserTestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTest
        fields = ['user', 'exam', 'language_code']

class UserTestCompleteSerializer(serializers.Serializer):
    completed_at = serializers.DateTimeField()
    answers = serializers.ListField(
        child=serializers.DictField(
            child=serializers.CharField()  # Для полей q_id, answer, isCorrect, date
        )
    )