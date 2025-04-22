from django.contrib import admin
from .models import UserAnswer


@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'test', 'variant_question', 'chosen_option_number', 'is_correct', 'answered_at')
    list_filter = ('is_correct', 'answered_at')
    search_fields = ('user__email', 'test__id', 'variant_question__question_text')