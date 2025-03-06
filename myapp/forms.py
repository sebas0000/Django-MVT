from django import forms

class CreateNewTask(forms.Form):
    text = forms.CharField(label="Titulo de tarea",max_length=200)
    priority = forms.IntegerField(label="Prioridad",required=False)
    