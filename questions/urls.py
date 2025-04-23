from django.urls import path
from .views import (
    QuestionListView, QuestionDetailView, QuestionCreateView, QuestionUpdateView,
    QuestionDeleteView, QuestionsBySectionView, AddOptionView, AddMultipleOptionsView, BulkQuestionCreateView, QuestionsByUserView
)

urlpatterns = [
    path('questions/', QuestionListView.as_view(), name='question-list'),
    path('questions/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
    path('questions/create/', QuestionCreateView.as_view(), name='question-create'),
    path('questions/<int:pk>/update/', QuestionUpdateView.as_view(), name='question-update'),
    path('questions/<int:pk>/delete/', QuestionDeleteView.as_view(), name='question-delete'),
    path('questions/by-section/<int:section_id>/', QuestionsBySectionView.as_view(), name='questions-by-section'),
    path('questions/by-user/<int:user_id>/', QuestionsByUserView.as_view(), name='questions-by-user'),
    path('questions/add-option/', AddOptionView.as_view(), name='add-option'),
    path('questions/add-options/', AddMultipleOptionsView.as_view(), name='add-options'),
    path('questions/creat/list/', BulkQuestionCreateView.as_view(), name='question-bulk-create'),
]