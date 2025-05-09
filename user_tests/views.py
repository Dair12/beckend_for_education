from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import UserTest, TestQuestion
from .serializers import UserTestSerializer, UserTestCreateSerializer, UserTestCompleteSerializer, TestQuestionSerializer
from questions.models import Question
import random

class UserTestViewSet(viewsets.ModelViewSet):
    queryset = UserTest.objects.all()
    serializer_class = UserTestSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return UserTestCreateSerializer
        elif self.action == 'complete':
            return UserTestCompleteSerializer
        return UserTestSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_test = serializer.save()

        # Extract validated data
        section = serializer.validated_data['section']
        language_code = serializer.validated_data['language_code']
        questions_count = serializer.validated_data['questions_count']
        level = serializer.validated_data.get('level')

        # Build the question query
        query = Question.objects.filter(section=section, language_code=language_code)
        if level:
            query = query.filter(level=level)

        # Select random questions
        questions = list(query)
        if len(questions) < questions_count:
            user_test.delete()  # Clean up the created test
            return Response({
                "error": f"Not enough questions available. Requested: {questions_count}, Available: {len(questions)}"
            }, status=status.HTTP_400_BAD_REQUEST)

        selected_questions = random.sample(questions, questions_count)
        for index, question in enumerate(selected_questions, start=1):
            TestQuestion.objects.create(
                test=user_test,
                variant_question=question,
                question_order=index
            )

        return Response({
            "message": "User test created successfully",
            "test": UserTestSerializer(user_test).data
        }, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['patch'], url_path='complete')
    def complete(self, request, pk=None):
        user_test = get_object_or_404(UserTest, pk=pk)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_test.completed_at = serializer.validated_data['completed_at']
        user_test.save()

        # Логика обработки ответов (пример)
        for answer in serializer.validated_data['answers']:
            # Здесь можно сохранить ответы в модель UserAnswer
            pass

        return Response({
            "message": f"User test {pk} completed successfully"
        }, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='user/(?P<user_id>\d+)')
    def by_user(self, request, user_id=None):
        tests = UserTest.objects.filter(user_id=user_id)
        serializer = self.get_serializer(tests, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path='questions')
    def test_questions(self, request, pk=None):
        test = get_object_or_404(UserTest, pk=pk)
        test_questions = TestQuestion.objects.filter(test=test)
        serializer = TestQuestionSerializer(test_questions, many=True)
        return Response(serializer.data)