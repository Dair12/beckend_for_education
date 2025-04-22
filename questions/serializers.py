from rest_framework import serializers
from .models import Question, QuestionType
from subjects.models import Subject, SubjectSection
from users.models import User

class QuestionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionType
        fields = ['id', 'name']

class QuestionSerializer(serializers.ModelSerializer):
    admin_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='admin')
    subject_id = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all(), source='subject')
    section_id = serializers.PrimaryKeyRelatedField(queryset=SubjectSection.objects.all(), source='section', allow_null=True)
    type_id = serializers.PrimaryKeyRelatedField(queryset=QuestionType.objects.all(), source='type', allow_null=True)

    class Meta:
        model = Question
        fields = [
            'id', 'admin_id', 'subject_id', 'section_id', 'question_text', 'image_path',
            'option_1', 'option_2', 'option_3', 'option_4', 'option_5', 'correct_option',
            'level', 'language_code', 'type_id', 'created_at'
        ]

class AddOptionSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    option_number = serializers.IntegerField(min_value=1, max_value=5)
    option_text = serializers.CharField(max_length=255)

class AddMultipleOptionsSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    options = serializers.DictField(child=serializers.CharField(max_length=255))