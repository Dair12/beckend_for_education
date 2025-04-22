from django.urls import path
from .views import (
    UserTestListView, UserTestDetailView, UserTestCreateView,
    UserTestCompleteView, UserTestsByUserView, TestQuestionsView
)

app_name = 'user_tests'

urlpatterns = [
    path('user-tests/', UserTestListView.as_view(), name='user-test-list'),
    path('user-tests/<int:id>/', UserTestDetailView.as_view(), name='user-test-detail'),
    path('user-tests/create/', UserTestCreateView.as_view(), name='user-test-create'),
    path('user-tests/<int:id>/complete/', UserTestCompleteView.as_view(), name='user-test-complete'),
    path('user-tests/user/<int:user_id>/', UserTestsByUserView.as_view(), name='user-tests-by-user'),
    path('test-questions/test/<int:test_id>/', TestQuestionsView.as_view(), name='test-questions'),
]