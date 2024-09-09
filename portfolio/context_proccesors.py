from datetime import datetime
from .models import Project
from blog.models import Post


def current_year(request):
    return {"current_year": datetime.now().year}


def latest_projects(request):
    latest_projects = Project.objects.all().order_by("-date")[:5]
    latest_posts = Post.objects.all().order_by("-date")[:5]
    data = {
        "latest_projects": latest_projects,
        "latest_posts": latest_posts,
    }
    return data
