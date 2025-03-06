from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404,render,redirect
from .forms import CreateNewTask,CreateNewProject
# Create your views here.
def index(request):
    title = 'Curso de Django'
    username = 'Contecon Manzanillo'
    return render(request,"index.html",{
        "title" : title,
        'username': username
    })

def login(request):
    return HttpResponse("<h2>Estas en el login dentro de la carpeta myapps</h2>")

def valor(request,username):
    print(username)
    return HttpResponse("<h2>Valor impreso en la consola: %s</h2>"%username)

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request,'Projects.html',{
        'projects':projects
    })

def tasks(request):
    #task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request,'tasks.html',{
        'tasks':tasks
    })

def create_task(request):
    if request.method == 'GET':
        return render(request,'create_task.html',{
        'form': CreateNewTask()
        })
    else:
        Task.objects.create(text=request.POST['text'],priority=request.POST['priority'],project_id=request.POST['project_id'])
        #print(request.GET['text'])
        #print(request.GET['priority'])
        return redirect('tasks')
    
def create_project(request):
    if request.method == 'GET':
        return render(request,'create_project.html',{
        'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('create_project')