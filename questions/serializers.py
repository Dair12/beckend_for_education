from rest_framework import serializers
from .models import Question
from exam_sections.models import Section
from users.models import User
import base64

class BulkQuestionCreateSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        questions = [Question(**item) for item in validated_data]
        return Question.objects.bulk_create(questions)

class Base64ImageField(serializers.Field):
    def to_internal_value(self, data):
        if not isinstance(data, str):
            raise serializers.ValidationError('Expected a base64 string')

        try:
            if ',' in data:
                data = data.split(',')[1]
            data = data.strip()
            data += '=' * (-len(data) % 4)  # padding
            return base64.b64decode(data)
        except Exception as e:
            raise serializers.ValidationError('Invalid base64 string')

    def to_representation(self, value):
        if value is None:
            return None
        return 'data:image/png;base64,' + base64.b64encode(value).decode('utf-8')

class QuestionSerializer(serializers.ModelSerializer):
    admin_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='admin')
    section_id = serializers.PrimaryKeyRelatedField(queryset=Section.objects.all(), source='section')

    question_image = Base64ImageField(required=False, allow_null=True)
    description_image = Base64ImageField(required=False, allow_null=True)

    def validate(self, data):
        section = data.get('section')
        position = data.get('position')
        if position and section:
            if position > section.default_question_count:
                raise serializers.ValidationError(
                    f"Position exceeds section's default_question_count ({section.default_question_count})."
                )
        return data

    class Meta:
        model = Question
        fields = [
            'id', 'admin_id', 'section_id', 'position', 'question_text', 'description', 'question_image',
            'description_image', 'option_1', 'option_2', 'option_3', 'option_4', 'option_5',
            'correct_option', 'level', 'language_code', 'created_at'
        ]

class AddOptionSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    option_number = serializers.IntegerField(min_value=1, max_value=5)
    option_text = serializers.CharField(max_length=255)

class AddMultipleOptionsSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    options = serializers.DictField(child=serializers.CharField(max_length=255))