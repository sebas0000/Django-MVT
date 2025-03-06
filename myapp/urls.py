from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("login/",views.login,name="login"),
    path("valor/<str:username>",views.valor,name="valor"),
    path("projects/",views.projects,name="projects"),
    path("tasks/",views.tasks,name="tasks"),
    path("create_task/",views.create_task,name="create_task"),
    path("create_project/",views.create_project,name="create_project")
    
]   