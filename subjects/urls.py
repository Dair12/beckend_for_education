from django.urls import path
from .views import (
    SubjectListView, SubjectDetailView, SubjectCreateView,
    SubjectSectionListView, SubjectSectionDetailView, SubjectSectionCreateView,
    SubjectSectionUpdateView, SubjectSectionDeleteView
)

app_name = 'subjects'

urlpatterns = [
    path('subjects/', SubjectListView.as_view(), name='subject-list'),
    path('subjects/<int:id>/', SubjectDetailView.as_view(), name='subject-detail'),
    path('subjects/create/', SubjectCreateView.as_view(), name='subject-create'),
    path('subject-sections/', SubjectSectionListView.as_view(), name='subject-section-list'),
    path('subject-sections/<int:id>/', SubjectSectionDetailView.as_view(), name='subject-section-detail'),
    path('subject-sections/create/', SubjectSectionCreateView.as_view(), name='subject-section-create'),
    path('subject-sections/<int:id>/update/', SubjectSectionUpdateView.as_view(), name='subject-section-update'),
    path('subject-sections/<int:id>/delete/', SubjectSectionDeleteView.as_view(), name='subject-section-delete'),
]