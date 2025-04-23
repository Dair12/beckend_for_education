from django.contrib import admin
from .models import Section

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('exam', 'subject', 'section', 'exam_code', 'has_fixed_structure', 'default_question_count', 'time_to_complete')
    list_filter = ('exam', 'subject', 'exam_code', 'has_fixed_structure')
    search_fields = ('exam', 'subject', 'section', 'exam_code')
    ordering = ('exam', 'subject', 'section')