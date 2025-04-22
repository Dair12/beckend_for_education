from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.shortcuts import get_object_or_404
from .models import Question, QuestionType
from .serializers import QuestionSerializer, QuestionTypeSerializer, AddOptionSerializer, AddMultipleOptionsSerializer
from subjects.models import Subject, SubjectSection

class QuestionListView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetailView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionCreateView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionUpdateView(generics.UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    partial = True

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class QuestionDeleteView(generics.DestroyAPIView):
    queryset = Question.objects.all()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": f"Question {instance.id} deleted successfully"}, status=status.HTTP_200_OK)

class QuestionsBySubjectView(generics.ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        subject_id = self.kwargs['subject_id']
        return Question.objects.filter(subject_id=subject_id)

class QuestionsBySectionView(generics.ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        section_id = self.kwargs['section_id']
        return Question.objects.filter(section_id=section_id)

class AddOptionView(APIView):
    def post(self, request):
        serializer = AddOptionSerializer(data=request.data)
        if serializer.is_valid():
            question = get_object_or_404(Question, id=serializer.validated_data['question_id'])
            option_number = serializer.validated_data['option_number']
            option_text = serializer.validated_data['option_text']
            setattr(question, f'option_{option_number}', option_text)
            question.save()
            return Response({"message": f"Option {option_number} added to question {question.id}"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddMultipleOptionsView(APIView):
    def post(self, request):
        serializer = AddMultipleOptionsSerializer(data=request.data)
        if serializer.is_valid():
            question = get_object_or_404(Question, id=serializer.validated_data['question_id'])
            options = serializer.validated_data['options']
            for option_number, option_text in options.items():
                if 1 <= int(option_number) <= 5:
                    setattr(question, f'option_{option_number}', option_text)
            question.save()
            return Response({"message": f"Options added to question {question.id}"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)