from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.utils import timezone
from .models import UserTest, TestQuestion
from .serializers import UserTestSerializer, UserTestCreateSerializer, TestQuestionSerializer
from questions.models import Question

class UserTestListView(generics.ListAPIView):
    queryset = UserTest.objects.all()
    serializer_class = UserTestSerializer

class UserTestDetailView(generics.RetrieveAPIView):
    queryset = UserTest.objects.all()
    serializer_class = UserTestSerializer
    lookup_field = 'id'

class UserTestCreateView(APIView):
    def post(self, request):
        serializer = UserTestCreateSerializer(data=request.data)
        if serializer.is_valid():
            user_test = serializer.save()
            # Automatically assign questions from the exam's subject
            questions = Question.objects.filter(subject__exam=user_test.exam)[:10]
            for idx, question in enumerate(questions, start=1):
                TestQuestion.objects.create(test=user_test, question=question, question_order=idx)
            return Response({
                'message': 'User test created successfully',
                'test': UserTestSerializer(user_test).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserTestCompleteView(APIView):
    def put(self, request, id):
        try:
            user_test = UserTest.objects.get(id=id)
            user_test.completed_at = timezone.now()
            user_test.save()
            return Response({'message': f'User test {id} completed successfully'}, status=status.HTTP_200_OK)
        except UserTest.DoesNotExist:
            return Response({'message': 'Test not found'}, status=status.HTTP_404_NOT_FOUND)

class UserTestsByUserView(generics.ListAPIView):
    serializer_class = UserTestSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return UserTest.objects.filter(user_id=user_id)

class TestQuestionsView(generics.ListAPIView):
    serializer_class = TestQuestionSerializer

    def get_queryset(self):
        test_id = self.kwargs['test_id']
        return TestQuestion.objects.filter(test_id=test_id)