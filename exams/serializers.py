from rest_framework import serializers
from .models import Exam
from subjects.models import Subject

class ExamSerializer(serializers.ModelSerializer):
    subjects = serializers.SerializerMethodField()

    class Meta:
        model = Exam
        fields = ['id', 'exam_code', 'name', 'has_fixed_structure', 'default_question_count', 'time_to_complete', 'created_at', 'subjects']

    def get_subjects(self, obj):
        return [subject.name for subject in obj.subjects.all()]

class ExamCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['exam_code', 'name', 'has_fixed_structure', 'default_question_count', 'time_to_complete']

    def validate_exam_code(self, value):
        if Exam.objects.filter(exam_code=value).exists():
            raise serializers.ValidationError("Exam code must be unique.")
        return value

class ExamStatisticsSerializer(serializers.Serializer):
    exam_id = serializers.IntegerField()
    tests_completed = serializers.IntegerField()
    average_score = serializers.FloatField()