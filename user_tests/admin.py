from django.contrib import admin
from .models import UserTest, TestQuestion

@admin.register(UserTest)
class UserTestAdmin(admin.ModelAdmin):
    list_display = ('user', 'section', 'language_code', 'created_at', 'completed_at')
    list_filter = ('section', 'language_code', 'completed_at')
    search_fields = ('user__email', 'section__exam', 'section__subject', 'section__section')
    list_select_related = ('user', 'section')
    ordering = ('created_at',)

@admin.register(TestQuestion)
class TestQuestionAdmin(admin.ModelAdmin):
    list_display = ('test', 'variant_question', 'question_order')
    list_filter = ('test__section',)
    search_fields = ('test__id', 'variant_question__question_text')
    list_select_related = ('test', 'variant_question')
    ordering = ('test', 'question_order')