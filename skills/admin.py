from django.contrib import admin
from .models import Skill


class SkillAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "image",
        "name",
        "experience",
    )
    list_filter = ("id", "name", "experience")
    search_fields = ("id", "name", "experience")


# Register your models here.
admin.site.register(Skill, SkillAdmin)
