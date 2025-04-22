from rest_framework import serializers
from .models import Subject, SubjectSection

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name']
        read_only_fields = ['id']

class SubjectSectionSerializer(serializers.ModelSerializer):
    subject_id = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all(), source='subject')

    class Meta:
        model = SubjectSection
        fields = ['id', 'subject_id', 'name']
        read_only_fields = ['id']