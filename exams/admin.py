from django.contrib import admin
from .models import Exam

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('exam_code', 'name', 'has_fixed_structure', 'default_question_count', 'time_to_complete', 'created_at')
    search_fields = ('exam_code', 'name')
    list_filter = ('has_fixed_structure', 'created_at')
    ordering = ('-created_at',)