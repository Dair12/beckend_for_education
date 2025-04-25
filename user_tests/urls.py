from django.urls import path
from .views import UserTestViewSet

urlpatterns = [
    # List all user tests
    path('user_tests/', UserTestViewSet.as_view({'get': 'list'}), name='user-test-list'),
    
    # Create a new user test
    path('user_tests/create/', UserTestViewSet.as_view({'post': 'create'}), name='user-test-create'),
    
    # Retrieve a specific user test
    path('user_tests/<int:pk>/', UserTestViewSet.as_view({'get': 'retrieve'}), name='user-test-detail'),
    
    # Update a specific user test (full update)
    path('user_tests/<int:pk>/update/', UserTestViewSet.as_view({'put': 'update'}), name='user-test-update'),
    
    # Partial update a specific user test
    path('user_tests/<int:pk>/partial-update/', UserTestViewSet.as_view({'patch': 'partial_update'}), name='user-test-partial-update'),
    
    # Delete a specific user test
    path('user_tests/<int:pk>/delete/', UserTestViewSet.as_view({'delete': 'destroy'}), name='user-test-delete'),
    
    # Complete a user test
    path('user_tests/<int:pk>/complete/', UserTestViewSet.as_view({'patch': 'complete'}), name='user-test-complete'),
    
    # Get tests by user ID
    path('user_tests/by-user/<int:user_id>/', UserTestViewSet.as_view({'get': 'by_user'}), name='user-tests-by-user'),
    
    # Get questions for a specific test
    path('user_tests/<int:pk>/questions/', UserTestViewSet.as_view({'get': 'test_questions'}), name='user-test-questions'),
]