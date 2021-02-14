from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListProjects, name='list-project'),
    path('project/create', views.CreateProject, name='create-project'),
]
