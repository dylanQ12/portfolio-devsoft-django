from django.contrib import admin
from .models import Project

# Model ProjectAdmin.
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "image",
        "title",
        "date",
    )
    list_filter = (
        "title",
        "date",
    )
    search_fields = ("id", "title", "description")
    date_hierarchy = "date"


admin.site.register(Project, ProjectAdmin)
