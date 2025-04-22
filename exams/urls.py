from django.urls import path
from .views import (
    ExamListView, ExamDetailView, ExamCreateView, ExamStatisticsView
)

app_name = 'exams'

urlpatterns = [
    path('exams/', ExamListView.as_view(), name='exam-list'),
    path('exams/<int:id>/', ExamDetailView.as_view(), name='exam-detail'),
    path('exams/create/', ExamCreateView.as_view(), name='exam-create'),
    path('statistics/exam/<int:exam_id>/', ExamStatisticsView.as_view(), name='exam-statistics'),
]