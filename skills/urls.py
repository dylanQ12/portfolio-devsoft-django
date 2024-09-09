from django.urls import path
from . import views


urlpatterns = [
    path("", views.skillsView, name="skills"),
    path("skill-detail/<int:id>", views.detailSkillView, name="skill-detail"),
]
