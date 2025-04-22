from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Exam
from .serializers import ExamSerializer, ExamStatisticsSerializer
from tests.models import UserTest, UserAnswer

class ExamListView(generics.ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

class ExamDetailView(generics.RetrieveAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    lookup_field = 'id'

class ExamCreateView(generics.CreateAPIView):
    serializer_class = ExamSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Exam created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExamUpdateView(generics.UpdateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        response = self.partial_update(request, *args, **kwargs)
        return Response({
            'message': f'Exam {self.kwargs["id"]} updated successfully'
        }, status=status.HTTP_200_OK)

class ExamDeleteView(generics.DestroyAPIView):
    queryset = Exam.objects.all()
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        response = self.destroy(request, *args, **kwargs)
        return Response({
            'message': f'Exam {self.kwargs["id"]} deleted successfully'
        }, status=status.HTTP_200_OK)

class ExamStatisticsView(APIView):
    def get(self, request, exam_id):
        try:
            exam = Exam.objects.get(id=exam_id)
            tests_completed = UserTest.objects.filter(exam_id=exam_id, completed_at__isnull=False).count()
            correct_answers = UserAnswer.objects.filter(test_id__exam_id=exam_id, is_correct=True).count()
            total_answers = UserAnswer.objects.filter(test_id__exam_id=exam_id).count()
            average_score = (correct_answers / total_answers) * 100 if total_answers > 0 else 0
            serializer = ExamStatisticsSerializer({
                'exam_id': exam_id,
                'tests_completed': tests_completed,
                'average_score': average_score
            })
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exam.DoesNotExist:
            return Response({'message': 'Exam not found'}, status=status.HTTP_404_NOT_FOUND)