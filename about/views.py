from django.shortcuts import render
from skills.models import Skill


# Create your views here.
def aboutView(request):
    skills = Skill.objects.all().order_by("-name")[:9]
    context = {
        "title": "Sobre mí",
        "skills": skills,
    }
    return render(request, "about-me.html", context)