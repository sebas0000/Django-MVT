from django import forms

class CreateNewTask(forms.Form):
    text = forms.CharField(label="Titulo de tarea",max_length=200)
    priority = forms.IntegerField(label="Prioridad",required=False)
    project_id = forms.IntegerField(label="Id del proyecto")

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del proyecto",max_length=200)