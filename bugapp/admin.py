from django.contrib import admin
from .models import Bug

@admin.register(Bug)
class BugAdmin(admin.ModelAdmin):
    list_display = ("title", "priority", "status", "reported_by", "assigned_to", "created_at")
    list_filter = ("priority", "status")
    search_fields = ("title", "description")
