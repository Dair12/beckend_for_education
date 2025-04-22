from django.urls import path
from .views import UserAnswerListCreateView, UserAnswersByTestView, UserAnswersByUserView, ResultSubmissionView

urlpatterns = [
    path('user-answers/', UserAnswerListCreateView.as_view(), name='user-answers-list-create'),
    path('user-answers/test/<int:test_id>/', UserAnswersByTestView.as_view(), name='user-answers-by-test'),
    path('user-answers/user/<int:user_id>/', UserAnswersByUserView.as_view(), name='user-answers-by-user'),
    path('results/submit/', ResultSubmissionView.as_view(), name='results-submit'),
]