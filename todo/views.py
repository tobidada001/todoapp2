from django.shortcuts import render, redirect
from .models import Task
from django.http import HttpResponse
# Create your views here.
def index(request):
    if request.method == 'POST':

        add = request.POST['add']
        date = request.POST['date']

        task = Task(task_name = add, task_date = date)
        task.save()

        print(add)
        print(date)

    data = Task.objects.all()
    return render(request, "index.html", {"data": data})

def somedata(request):
    print('TThis is somee example\n')
    return redirect('/')


def delete(request, id):
    print('You deleted data\n')

    if request.method == 'POST':
        print('Its a get request')
        d = Task.objects.get(id = id)
        d.delete()
        print(d,'has been deleted')
        

    return redirect('/')

def confirm(request, id):
    print('You confirmed data\n')

    if request.method == 'POST':
        print('Its a post request')
        d = Task.objects.get(id = id)
        d.status = 'Finished'

        d.save()
        print(d,'has been finished')

    return redirect('/')