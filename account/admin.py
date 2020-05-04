from django.contrib import admin
from . import models


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'is_active', ]
    list_editable = ['is_active', ]
    search_fields = ['user', 'name', ]
    list_filter = ['user', 'name', 'created', ]
