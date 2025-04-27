from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserAnswer
from user_tests.models import UserTest
from questions.models import Question
from users.models import User
from questions.serializers import QuestionSerializer  # Import QuestionSerializer

class UserAnswerSerializer(serializers.ModelSerializer):
    variant_question = QuestionSerializer(read_only=True)  # Include full question details

    class Meta:
        model = UserAnswer
        fields = ['id', 'test', 'variant_question', 'user', 'chosen_option_number', 'is_correct', 'answered_at']
        read_only_fields = ['id', 'is_correct', 'answered_at']

    def validate(self, data):
        question = data['variant_question']
        if data['chosen_option_number'] not in range(1, 6) or (
            question.option_5 is None and data['chosen_option_number'] == 5
        ) or (
            question.option_4 is None and data['chosen_option_number'] >= 4
        ) or (
            question.option_3 is None and data['chosen_option_number'] >= 3
        ):
            raise serializers.ValidationError("Invalid chosen option number for this question.")

        if data['test'].user != data['user']:
            raise serializers.ValidationError("Test does not belong to this user.")

        data['is_correct'] = data['chosen_option_number'] == question.correct_option
        return data

class AnswerItemSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    chosen_option = serializers.IntegerField()
    is_correct = serializers.BooleanField()

class ResultSubmissionSerializer(serializers.Serializer):
    test_id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    answers = AnswerItemSerializer(many=True)

    def validate(self, data):
        test = UserTest.objects.filter(id=data['test_id']).first()
        if not test:
            raise serializers.ValidationError("Test does not exist.")

        user = User.objects.filter(id=data['user_id']).first()
        if not user:
            raise serializers.ValidationError("User does not exist in users model.")

        if test.user != user:
            raise serializers.ValidationError("Test does not belong to this user.")

        for answer in data['answers']:
            if 'question_id' not in answer or 'chosen_option' not in answer:
                raise serializers.ValidationError("Each answer must contain 'question_id' and 'chosen_option'.")

            question_id = answer['question_id']
            chosen_option = answer['chosen_option']

            question = Question.objects.filter(id=question_id).first()
            if not question:
                raise serializers.ValidationError(f"Question {question_id} does not exist.")

            if chosen_option not in range(1, 6):
                raise serializers.ValidationError(f"Invalid chosen option {chosen_option} for question {question_id}.")

        return data