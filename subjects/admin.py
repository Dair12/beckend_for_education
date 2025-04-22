from django.contrib import admin
from .models import Subject, SubjectSection

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(SubjectSection)
class SubjectSectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'name')
    list_filter = ('subject',)
    search_fields = ('name', 'subject__name')
    ordering = ('subject', 'name')