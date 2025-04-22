from rest_framework import serializers
from .models import Exam

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['id', 'exam_code', 'name', 'has_fixed_structure', 'default_question_count', 'time_to_complete', 'created_at']
        read_only_fields = ['id', 'created_at']

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