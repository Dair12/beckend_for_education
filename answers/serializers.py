from rest_framework import serializers
from .models import UserAnswer
from users.models import User
from user_tests.models import UserTest
from questions.models import Question

class UserAnswerSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    test = serializers.PrimaryKeyRelatedField(queryset=UserTest.objects.all())
    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())

    class Meta:
        model = UserAnswer
        fields = ['id', 'test', 'question', 'user', 'chosen_option_number', 'is_correct', 'answered_at']
        read_only_fields = ['id', 'answered_at']