from rest_framework import serializers
from .models import UserAnswer
from tests.models import UserTest
from questions.models import Question
from users.models import User


class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = ['id', 'test', 'variant_question', 'user', 'chosen_option_number', 'is_correct', 'answered_at']
        read_only_fields = ['id', 'is_correct', 'answered_at']

    def validate(self, data):
        # Проверка, что выбранный вариант ответа валиден для вопроса
        question = data['variant_question']
        if data['chosen_option_number'] not in range(1, 6) or (
            question.option_5 is None and data['chosen_option_number'] == 5
        ) or (
            question.option_4 is None and data['chosen_option_number'] >= 4
        ) or (
            question.option_3 is None and data['chosen_option_number'] >= 3
        ):
            raise serializers.ValidationError("Invalid chosen option number for this question.")
        
        # Проверка, что тест принадлежит пользователю
        if data['test'].user != data['user']:
            raise serializers.ValidationError("Test does not belong to this user.")
        
        # Автоматически определяем правильность ответа
        data['is_correct'] = data['chosen_option_number'] == question.correct_option
        return data


class ResultSubmissionSerializer(serializers.Serializer):
    test_id = serializers.IntegerField()
    answers = serializers.ListField(
        child=serializers.DictField(
            child=serializers.IntegerField(),
            required_fields=['question_id', 'chosen_option']
        )
    )

    def validate(self, data):
        test = UserTest.objects.filter(id=data['test_id']).first()
        if not test:
            raise serializers.ValidationError("Test does not exist.")
        
        for answer in data['answers']:
            question = Question.objects.filter(id=answer['question_id']).first()
            if not question:
                raise serializers.ValidationError(f"Question {answer['question_id']} does not exist.")
            if answer['chosen_option'] not in range(1, 6):
                raise serializers.ValidationError(f"Invalid chosen option for question {answer['question_id']}.")
        return data