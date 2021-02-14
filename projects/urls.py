from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListProjects, name='list-project'),
    path('project/create', views.CreateProject, name='create-project'),
    path('project/delete/<int:id>/', views.DeleteProject, name='delete-project'),
    path('project/edit/<int:id>/', views.EditProject, name='edit-project'),
    path('project/<int:id>/', views.DetailProject, name='detail-project'),
]
