from rest_framework import generics
from .models import Section
from .serializers import SectionSerializer

class SectionCreateView(generics.CreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

    def perform_create(self, serializer):
        # Сохраняем новый раздел
        section = serializer.save()

# Просмотр всех элементов таблицы Section
class SectionListView(generics.ListAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer