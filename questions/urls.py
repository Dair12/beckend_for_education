from django.urls import path
from .views import (
    QuestionListView, QuestionDetailView, QuestionCreateView, QuestionUpdateView,
    QuestionDeleteView, QuestionsBySubjectView, QuestionsBySectionView,
    AddOptionView, AddMultipleOptionsView
)

urlpatterns = [
    path('', QuestionListView.as_view(), name='question-list'),
    path('<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
    path('create/', QuestionCreateView.as_view(), name='question-create'),
    path('<int:pk>/update/', QuestionUpdateView.as_view(), name='question-update'),
    path('<int:pk>/delete/', QuestionDeleteView.as_view(), name='question-delete'),
    path('by-subject/<int:subject_id>/', QuestionsBySubjectView.as_view(), name='questions-by-subject'),
    path('by-section/<int:section_id>/', QuestionsBySectionView.as_view(), name='questions-by-section'),
    path('add-option/', AddOptionView.as_view(), name='add-option'),
    path('add-options/', AddMultipleOptionsView.as_view(), name='add-options'),
]