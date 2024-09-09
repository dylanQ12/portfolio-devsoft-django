from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "image",
        "title",
        "date",
    )
    list_filter = (
        "id",
        "title",
        "date",
    )
    search_fields = ("id", "title")
    date_hierarchy = "date"


admin.site.register(Post, PostAdmin)
