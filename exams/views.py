from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.shortcuts import get_object_or_404
from .models import Exam
from .serializers import ExamSerializer, ExamCreateSerializer, ExamStatisticsSerializer
from user_tests.models import UserTest  # Предполагается, что модель UserTest в приложении tests
from answers.models import UserAnswer  # Предполагается, что модель UserAnswer в приложении answers
from django.db.models import Count, Avg

class ExamListView(generics.ListAPIView):
    """Список всех экзаменов."""
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

class ExamDetailView(generics.RetrieveAPIView):
    """Данные одного экзамена."""
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    lookup_url_kwarg = 'id'

class ExamCreateView(APIView):
    """Создание нового экзамена."""
    def post(self, request):
        serializer = ExamCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Exam created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExamStatisticsView(APIView):
    """Статистика по экзамену."""
    def get(self, request, exam_id):
        # Проверяем, существует ли экзамен
        exam = get_object_or_404(Exam, id=exam_id)
        
        # Количество завершённых тестов
        tests_completed = UserTest.objects.filter(exam_id=exam_id, completed_at__isnull=False).count()
        
        # Средний балл (предполагается, что UserAnswer хранит информацию о правильности ответа)
        average_score = UserAnswer.objects.filter(
            test_id__exam_id=exam_id,
            test_id__completed_at__isnull=False
        ).aggregate(avg_score=Avg('is_correct'))['avg_score'] or 0.0
        
        data = {
            "exam_id": exam_id,
            "tests_completed": tests_completed,
            "average_score": average_score * 100 if average_score else 0.0  # Конвертация в проценты
        }
        
        serializer = ExamStatisticsSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)