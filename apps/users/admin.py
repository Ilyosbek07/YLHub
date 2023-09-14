from django.contrib import admin

from apps.users.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name']
    list_filter = ['user']
    search_fields = ['user']


admin.site.register(Profile, ProfileAdmin)
