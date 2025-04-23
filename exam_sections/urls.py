from django.urls import path
from .views import SectionListView, SectionCreateView

app_name = 'exam_sections'

urlpatterns = [
    path('sections/', SectionListView.as_view(), name='section-list'),  # Просмотр всех элементов
    path('sections/create/', SectionCreateView.as_view(), name='section-create'),  # Добавление нового раздела
]