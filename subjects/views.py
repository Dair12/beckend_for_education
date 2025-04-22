from rest_framework import generics
from .models import Subject, SubjectSection
from .serializers import SubjectSerializer, SubjectSectionSerializer

class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    lookup_field = 'id'

class SubjectCreateView(generics.CreateAPIView):
    serializer_class = SubjectSerializer

class SubjectSectionListView(generics.ListAPIView):
    queryset = SubjectSection.objects.all()
    serializer_class = SubjectSectionSerializer

class SubjectSectionDetailView(generics.RetrieveAPIView):
    queryset = SubjectSection.objects.all()
    serializer_class = SubjectSectionSerializer
    lookup_field = 'id'

class SubjectSectionCreateView(generics.CreateAPIView):
    serializer_class = SubjectSectionSerializer

class SubjectSectionUpdateView(generics.UpdateAPIView):
    queryset = SubjectSection.objects.all()
    serializer_class = SubjectSectionSerializer
    lookup_field = 'id'

class SubjectSectionDeleteView(generics.DestroyAPIView):
    queryset = SubjectSection.objects.all()
    lookup_field = 'id'