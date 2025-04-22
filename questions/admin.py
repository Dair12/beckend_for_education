from django.contrib import admin
from .models import Question, QuestionType

@admin.register(QuestionType)
class QuestionTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question_text', 'subject', 'level', 'language_code', 'created_at']
    list_filter = ['level', 'language_code', 'subject', 'type']
    search_fields = ['question_text']
    raw_id_fields = ['admin', 'subject', 'section', 'type']