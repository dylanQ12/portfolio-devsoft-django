from django.shortcuts import render, get_object_or_404
from .models import Skill


def skillsView(request):
    skills = Skill.objects.all()
    context = {
        "title": "Habilidades",
        "skills": skills,
    }
    return render(request, "skills.html", context)


def detailSkillView(request, id):
    skill = get_object_or_404(Skill, pk=id)
    context = {
        "title": skill.name,
        "skill": skill,
    }
    return render(request, "detail-skill.html", context)

