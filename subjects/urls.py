from django.urls import path
from .views import (
    SubjectListCreateView, SubjectDetailView,
    SubjectSectionListCreateView, SubjectSectionDetailView,
    SubjectSectionUpdateView, SubjectSectionDeleteView
)

app_name = 'subjects'

urlpatterns = [
    # Предметы
    path('subjects/', SubjectListCreateView.as_view(), name='subject-list-create'),
    path('subjects/<int:pk>/', SubjectDetailView.as_view(), name='subject-detail'),
    path('subjects/create/', SubjectListCreateView.as_view(), name='subject-create'),  # POST для создания

    # Разделы предметов
    path('subject-sections/', SubjectSectionListCreateView.as_view(), name='section-list-create'),
    path('subject-sections/<int:pk>/', SubjectSectionDetailView.as_view(), name='section-detail'),
    path('subject-sections/create/', SubjectSectionListCreateView.as_view(), name='section-create'),
    path('subject-sections/<int:pk>/update/', SubjectSectionUpdateView.as_view(), name='section-update'),
    path('subject-sections/<int:pk>/delete/', SubjectSectionDeleteView.as_view(), name='section-delete'),
]