from django.urls import path
from .views import (
    LoginView, RegisterView, UserListView, UserDetailView,
    UserUpdateView, UserDeleteView, UserStatisticsView
)

app_name = 'users'

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:id>/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:id>/update/', UserUpdateView.as_view(), name='user-update'),
    path('users/<int:id>/delete/', UserDeleteView.as_view(), name='user-delete'),
    path('statistics/user/<int:user_id>/', UserStatisticsView.as_view(), name='user-statistics'),
]