from django.contrib import admin

from accounts.models import ProfileModel


@admin.register(ProfileModel)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'gender', 'phone', 'created_at']
    search_fields = ['user', 'phone']
    list_filter = ['created_at', 'gender']
