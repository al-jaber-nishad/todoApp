from django.shortcuts import render, redirect
from tasks.forms import task_infoForm
from .models import task_info
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):

  form = task_infoForm()
  tasks = task_info.objects.all()


  if request.method == 'POST':

    form = task_infoForm(request.POST)

    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/')
  
  return render(request, 'tasks/index.html', {'form': form, 'tasks':tasks})


def updateTask(request, pk):
  tasks = task_info.objects.get(id=pk)

  form = task_infoForm(instance=tasks)

  if request.method == 'POST':

    form = task_infoForm(request.POST, instance=tasks)

    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/')


  context = {'form':form, }
  return render(request, 'tasks/update.html', context)

def deleteTask(request, pk):
  item = task_info.objects.get(id=pk)

  if request.method == 'POST':
    item.delete()
    return HttpResponseRedirect('/')

  context = {'item': item}

  return render(request, 'tasks/delete.html', context)