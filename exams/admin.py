from django.contrib import admin
from .models import Exam

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('id', 'exam_code', 'name', 'has_fixed_structure', 'default_question_count', 'time_to_complete')
    list_filter = ('has_fixed_structure',)
    search_fields = ('name', 'exam_code')