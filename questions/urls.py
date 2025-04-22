from django.urls import path
from .views import (
    QuestionListView, QuestionDetailView, QuestionCreateView,
    QuestionUpdateView, QuestionDeleteView
)

app_name = 'questions'

urlpatterns = [
    path('questions/', QuestionListView.as_view(), name='question-list'),
    path('questions/<int:id>/', QuestionDetailView.as_view(), name='question-detail'),
    path('questions/create/', QuestionCreateView.as_view(), name='question-create'),
    path('questions/<int:id>/update/', QuestionUpdateView.as_view(), name='question-update'),
    path('questions/<int:id>/delete/', QuestionDeleteView.as_view(), name='question-delete'),
]