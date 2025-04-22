from rest_framework import serializers
from .models import Subject, SubjectSection
from exams.models import Exam

class SubjectSerializer(serializers.ModelSerializer):
    exam_id = serializers.PrimaryKeyRelatedField(
        queryset=Exam.objects.all(), source='exams', write_only=True
    )

    class Meta:
        model = Subject
        fields = ['id', 'name', 'exam_id']

    def create(self, validated_data):
        exam = validated_data.pop('exams')
        subject = Subject.objects.create(**validated_data)
        subject.exams.add(exam)
        return subject

class SubjectSectionSerializer(serializers.ModelSerializer):
    subject_id = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all(), source='subject')

    class Meta:
        model = SubjectSection
        fields = ['id', 'subject_id', 'name']