from rest_framework import serializers
from .models import Section

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id', 'exam', 'subject', 'section', 'exam_code', 'has_fixed_structure', 'default_question_count', 'time_to_complete']