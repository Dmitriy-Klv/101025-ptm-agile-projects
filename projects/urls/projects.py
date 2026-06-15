from django.urls import path

from projects.views.projects import ProjectsListAPIView


urlpatterns = [
    path('', ProjectsListAPIView.as_view()),
]
