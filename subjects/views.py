from rest_framework import generics, status
from rest_framework.response import Response
from .models import Subject, SubjectSection
from .serializers import SubjectSerializer, SubjectSectionSerializer

# Список и создание предметов
class SubjectListCreateView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {"message": "Subject created successfully"},
            status=status.HTTP_201_CREATED
        )

# Детали предмета
class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

# Список и создание разделов
class SubjectSectionListCreateView(generics.ListCreateAPIView):
    queryset = SubjectSection.objects.all()
    serializer_class = SubjectSectionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {"message": "Subject section created successfully"},
            status=status.HTTP_201_CREATED
        )

# Детали раздела
class SubjectSectionDetailView(generics.RetrieveAPIView):
    queryset = SubjectSection.objects.all()
    serializer_class = SubjectSectionSerializer

# Обновление раздела
class SubjectSectionUpdateView(generics.UpdateAPIView):
    queryset = SubjectSection.objects.all()
    serializer_class = SubjectSectionSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {"message": f"Subject section {instance.id} updated successfully"},
            status=status.HTTP_200_OK
        )

# Удаление раздела
class SubjectSectionDeleteView(generics.DestroyAPIView):
    queryset = SubjectSection.objects.all()
    serializer_class = SubjectSectionSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": f"Subject section {instance.id} deleted successfully"},
            status=status.HTTP_200_OK
        )