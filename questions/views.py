from rest_framework import generics, status
from rest_framework.response import Response
from .models import Question
from .serializers import QuestionSerializer

class QuestionListView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetailView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'id'

class QuestionCreateView(generics.CreateAPIView):
    serializer_class = QuestionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Question created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionUpdateView(generics.UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        response = self.partial_update(request, *args, **kwargs)
        return Response({'message': f'Question {self.kwargs["id"]} updated successfully'}, status=status.HTTP_200_OK)

class QuestionDeleteView(generics.DestroyAPIView):
    queryset = Question.objects.all()
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        response = self.destroy(request, *args, **kwargs)
        return Response({'message': f'Question {self.kwargs["id"]} deleted successfully'}, status=status.HTTP_200_OK)