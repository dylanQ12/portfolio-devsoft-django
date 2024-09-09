from django.urls import path
from . import views


urlpatterns = [
    path("", views.homeView, name="home"),
    path("portfolio/projects/", views.portfolioView, name="portfolio"),
    path("portfolio/project/<int:id>/", views.projectDetailView, name="project-detail"),
]
