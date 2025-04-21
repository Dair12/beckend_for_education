from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'role', 'created_at')
    list_filter = ('role', 'created_at')
    search_fields = ('name', 'email')
    readonly_fields = ('created_at',)