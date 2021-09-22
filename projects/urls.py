from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_index, name="project_index"), #root URL for website
    path("<int:pk>/", views.project_detail, name="project_detail"), #dinamicaly created url with int for pk of specific project
]