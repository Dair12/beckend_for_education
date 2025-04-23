from rest_framework import generics
from .models import Section
from .serializers import SectionSerializer

# Просмотр всех элементов таблицы Section
class SectionListView(generics.ListAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

# Добавление нового раздела
class SectionCreateView(generics.CreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

    def perform_create(self, serializer):
        serializer.save()