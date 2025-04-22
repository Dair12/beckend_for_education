from django.contrib import admin
from .models import UserTest, TestQuestion

@admin.register(UserTest)
class UserTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'exam', 'language_code', 'created_at', 'completed_at')
    list_filter = ('exam', 'language_code', 'completed_at')
    search_fields = ('user__name', 'exam__name')

@admin.register(TestQuestion)
class TestQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'test', 'variant_question', 'question_order')
    list_filter = ('test__exam',)
    search_fields = ('variant_question__question_text',)