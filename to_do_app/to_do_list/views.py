from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .forms import TaskForm
from .models import Task
import logging
logging = logging.getLogger('main')


def index(request):
    todos = Task.objects.filter(user=request.user).order_by('-created')
    q = request.GET.get('q')
    if q:
        todos = todos.filter(title__icontains=q)  # Поиск по названию задачи (без учета регистра)

    context = {
             'todo_list': todos
             }
    return render(request, 'to_do_app/index.html', context)


def edit_todo(request, todo_id):
    todo = Task.objects.get(id=todo_id, user=request.user)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('tasks:index')
    else:
        form = TaskForm(instance=todo)
    return render(request, 'to_do_app/edit.html', {'todo': todo, 'form': form})


@require_http_methods(['POST'])
def add(request):
    title = request.POST['title']
    todo = Task.objects.create(title=title, user=request.user)
    todo.save()
    logging.info(f'Задача "{title}" добавлена пользователем {request.user.username}')
    return redirect('tasks:index')


def delete(request, todo_id):
    todo = Task.objects.get(id=todo_id, user=request.user)
    todo.delete()
    return redirect('tasks:index')


def completed(request, todo_id):
    todo = Task.objects.get(id=todo_id, user=request.user)
    todo.is_completed = not todo.is_completed
    todo.save()
    return redirect('tasks:index')



