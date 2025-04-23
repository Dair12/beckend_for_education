from django.contrib import admin
from .models import Question, QuestionType

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text_short', 'section', 'level', 'language_code', 'created_at')
    list_filter = ('section', 'level', 'language_code')
    search_fields = ('question_text', 'section__exam', 'section__subject', 'section__section')
    list_select_related = ('section',)
    ordering = ('section', 'created_at')

    def question_text_short(self, obj):
        return obj.question_text[:50] + ('...' if len(obj.question_text) > 50 else '')
    question_text_short.short_description = 'Question Text'

@admin.register(QuestionType)
class QuestionTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'section', 'position')
    list_filter = ('section',)
    search_fields = ('name', 'section__exam', 'section__subject', 'section__section')
    list_select_related = ('section',)
    ordering = ('section', 'position')