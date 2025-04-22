from rest_framework import serializers
from .models import Exam

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['id', 'exam_code', 'name', 'has_fixed_structure', 'default_question_count', 'time_to_complete']
        read_only_fields = ['id']

class ExamStatisticsSerializer(serializers.Serializer):
    exam_id = serializers.IntegerField()
    tests_completed = serializers.IntegerField()
    average_score = serializers.FloatField()