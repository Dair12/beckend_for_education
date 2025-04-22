from django.contrib import admin
from .models import UserTest, TestQuestion

@admin.register(UserTest)
class UserTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'exam', 'language_code', 'created_at', 'completed_at')
    list_filter = ('exam', 'language_code', 'completed_at')
    search_fields = ('user__email', 'exam__name')

@admin.register(TestQuestion)
class TestQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'test', 'question', 'question_order')
    list_filter = ('test',)
    search_fields = ('question__question_text',)