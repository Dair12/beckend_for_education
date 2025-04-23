from rest_framework import generics
from .models import Section
from  questions.models import QuestionType
from .serializers import SectionSerializer

class SectionCreateView(generics.CreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

    def perform_create(self, serializer):
        # Сохраняем новый раздел
        section = serializer.save()
        # Создаём QuestionType для каждого position от 1 до default_question_count
        for position in range(1, section.default_question_count + 1):
            QuestionType.objects.create(
                section=section,
                position=position,
                name=f"Type {position}"  # Можно заменить на другое имя, если нужно
            )

# Просмотр всех элементов таблицы Section
class SectionListView(generics.ListAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer