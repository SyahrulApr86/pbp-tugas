from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from todolist.models import Task
from todolist.forms import TaskForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')

    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return redirect('todolist:login')

@login_required(login_url='todolist:login')
def show_todolist(request):
    data_task = Task.objects.filter(user=request.user)
    nama = request.user.username
    context = {
        'list_task': data_task,
        'nama': nama,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, 'todolist.html', context)

def hapus(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('todolist:show_todolist')

def ubah_status(request, pk):
    todolist = Task.objects.get(pk=pk)
    if todolist.is_finished:
        todolist.is_finished = False
    else:
        todolist.is_finished = True
    todolist.save()
    return redirect('todolist:show_todolist')

def tambah(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        new_task = Task(task=task)
        new_task.save()
        return redirect('todolist:show_todolist')
    context = {}
    return render(request, 'tambah.html', context)

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = Task(
                user = request.user,
                date = request.POST.get('date'),
                title = request.POST.get('title'),
                description = request.POST.get('description'),
            )
            task.save()
            return redirect('todolist:show_todolist')
    else:
        form = TaskForm()

        context = {'form':form}
        return render(request, 'create_task.html', context)