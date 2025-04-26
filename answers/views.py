from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.utils import timezone
from django.contrib.auth import get_user_model
from .models import UserAnswer
from .serializers import UserAnswerSerializer, ResultSubmissionSerializer
from user_tests.models import UserTest
from users.models import User
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
            user_id = serializer.validated_data['user_id']
            answers = serializer.validated_data['answers']

            try:
                test = UserTest.objects.get(id=test_id)
                user = User.objects.get(id=user_id)  # Вот здесь из users.models.User
            except UserTest.DoesNotExist:
                return Response({"error": "Test does not exist"}, status=status.HTTP_400_BAD_REQUEST)
            except User.DoesNotExist:
                return Response({"error": "User does not exist"}, status=status.HTTP_400_BAD_REQUEST)

            response_data = {
                "test_id": test_id,
                "user_id": user_id,
                "section": test.section.subject,
                "language_code": test.language_code,
                "created_at": test.created_at,
                "completed_at": test.completed_at,
                "total_questions": 0,
                "correct_answers": 0,
                "incorrect_answers": 0,
                "answers": []
            }

            with transaction.atomic():
                for answer_data in answers:
                    question_id = answer_data['question_id']
                    chosen_option = answer_data['chosen_option']
                    is_correct = answer_data['is_correct']

                    try:
                        question = Question.objects.get(id=question_id)
                    except Question.DoesNotExist:
                        return Response(
                            {"error": f"Question {question_id} does not exist"},
                            status=status.HTTP_400_BAD_REQUEST
                        )
                    is_correct = answer_data['is_correct']

                    UserAnswer.objects.create(
                        test=test,
                        variant_question=question,
                        user=user,
                        chosen_option_number=chosen_option,
                        is_correct=is_correct
                    )

                    response_data["answers"].append({
                        "question_id": question_id,
                        "chosen_option": chosen_option,
                        "correct_option": question.correct_option,
                        "is_correct": is_correct,
                        "question_text": question.question_text
                    })
                    response_data["total_questions"] += 1
                    if is_correct:
                        response_data["correct_answers"] += 1
                    else:
                        response_data["incorrect_answers"] += 1

                if not test.completed_at:
                    test.completed_at = timezone.now()
                    test.save()

            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

