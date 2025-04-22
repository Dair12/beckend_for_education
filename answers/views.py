from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import UserAnswer
from .serializers import UserAnswerSerializer, ResultSubmissionSerializer
from tests.models import UserTest
from django.db import transaction
from questions.models import Question


class UserAnswerListCreateView(generics.ListCreateAPIView):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserAnswersByTestView(generics.ListAPIView):
    serializer_class = UserAnswerSerializer

    def get_queryset(self):
        test_id = self.kwargs['test_id']
        return UserAnswer.objects.filter(test_id=test_id)


class UserAnswersByUserView(generics.ListAPIView):
    serializer_class = UserAnswerSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return UserAnswer.objects.filter(user_id=user_id)


class ResultSubmissionView(APIView):
    def post(self, request):
        serializer = ResultSubmissionSerializer(data=request.data)
        if serializer.is_valid():
            test_id = serializer.validated_data['test_id']
            answers = serializer.validated_data['answers']
            test = UserTest.objects.get(id=test_id)

            with transaction.atomic():
                for answer_data in answers:
                    question_id = answer_data['question_id']
                    chosen_option = answer_data['chosen_option']
                    question = Question.objects.get(id=question_id)
                    is_correct = chosen_option == question.correct_option

                    UserAnswer.objects.create(
                        test=test,
                        variant_question=question,
                        user=request.user,
                        chosen_option_number=chosen_option,
                        is_correct=is_correct
                    )

            return Response(
                {"message": "Results submitted successfully"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)