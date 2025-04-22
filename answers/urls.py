from django.urls import path
from .views import (
    UserAnswerListView, UserAnswerCreateView,
    UserAnswersByTestView, UserAnswersByUserView,
    SubmitResultsView
)

app_name = 'answers'

urlpatterns = [
    path('user-answers/', UserAnswerListView.as_view(), name='user-answer-list'),
    path('user-answers/create/', UserAnswerCreateView.as_view(), name='user-answer-create'),
    path('user-answers/test/<int:test_id>/', UserAnswersByTestView.as_view(), name='user-answers-by-test'),
    path('user-answers/user/<int:user_id>/', UserAnswersByUserView.as_view(), name='user-answers-by-user'),
    path('results/submit/', SubmitResultsView.as_view(), name='submit-results'),
]