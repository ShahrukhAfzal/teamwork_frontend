from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListProjects, name='list-project'),
    path('project/create', views.CreateProject, name='create-project'),
    path('project/delete/<int:id>/', views.DeleteProject, name='delete-project'),
    path('project/edit/<int:id>/', views.EditProject, name='edit-project'),
    path('project/detail/<int:id>/', views.DetailProject, name='detail-project'),

    path('project/<int:id>/task/create/', views.CreateTask, name='create-task'),
    path('project/<int:project_id>/task/<int:task_id>/', views.DetailTask, name='detail-task'),
    path('project/<int:project_id>/task/edit/<int:task_id>/', views.EditTask, name='edit-task'),
    path('project/<int:project_id>/task/delete/<int:task_id>/', views.DeleteTask, name='delete-task'),
]
