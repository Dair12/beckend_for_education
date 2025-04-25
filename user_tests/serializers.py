from rest_framework import serializers
from .models import UserTest, TestQuestion
from questions.serializers import QuestionSerializer
from users.serializers import UserSerializer
from exam_sections.serializers import SectionSerializer
from users.models import User
from exam_sections.models import Section
from questions.models import Question

class TestQuestionSerializer(serializers.ModelSerializer):
    variant_question = QuestionSerializer()

    class Meta:
        model = TestQuestion
        fields = ['id', 'variant_question', 'question_order']

class UserTestSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    section = SectionSerializer(read_only=True)
    test_questions = TestQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = UserTest
        fields = ['id', 'user', 'section', 'language_code', 'created_at', 'completed_at', 'test_questions']

class UserTestCreateSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user')
    section_id = serializers.PrimaryKeyRelatedField(queryset=Section.objects.all(), source='section')
    questions_count = serializers.IntegerField(min_value=1, required=False, default=20)
    level = serializers.ChoiceField(choices=Question.LEVEL_CHOICES, required=False, allow_null=True)

    def create(self, validated_data):
        # Extract model fields only
        model_data = {
            'user': validated_data['user'],
            'section': validated_data['section'],
            'language_code': validated_data['language_code']
        }
        # Create UserTest instance with valid model fields
        user_test = UserTest.objects.create(**model_data)
        return user_test

    class Meta:
        model = UserTest
        fields = ['user_id', 'section_id', 'language_code', 'questions_count', 'level']

class UserTestCompleteSerializer(serializers.Serializer):
    completed_at = serializers.DateTimeField()
    answers = serializers.ListField(
        child=serializers.DictField(
            child=serializers.CharField()
        )
    )