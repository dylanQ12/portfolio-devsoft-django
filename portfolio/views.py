from django.shortcuts import get_object_or_404, render
from .models import Project
from blog.models import Post
from skills.models import Skill


# Create your views here.
def homeView(request):
    # Ordenar proyectos y posts por fecha y limitar a 9 elementos
    projects = Project.objects.all().order_by("-date")[:9]
    posts = Post.objects.all().order_by("-date")[:9]
    skills = Skill.objects.all().order_by("-name")[:9]
    
    
    context = {
        "title": "Inicio",
        "projects": projects,
        "posts": posts,
        "skills": skills,
    }
    return render(request, "home.html", context)


def portfolioView(request):
    projects = Project.objects.order_by("-date")
    total_projects = Project.objects.count()
    context = {
        "title": "Portafolio",
        "projects": projects,
        "total_projects": total_projects,
    }
    return render(request, "portfolio.html", context)


def projectDetailView(request, id):
    project = get_object_or_404(Project, pk=id)
    context = {
        "title": project.title,
        "project": project,
    }
    return render(request, "project-detail.html", context)
