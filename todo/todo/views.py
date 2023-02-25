from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm


def todo_list(request):
    todos = Todo.objects.filter(complete=False)
    context = {'todos': todos}
    return render(request, 'todo/todo_list.html', context)


def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    context = {'todo': todo}
    return render(request, 'todo/todo_detail.html', context)


def todo_post(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=True)
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()

    return render(request, 'todo/todo_post.html', {'form': form})


def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_post.html', {'form': form})


def done_list(request):
    dones = Todo.objects.filter(complete=True)
    render(request, 'todo/done_list.html', {'dones': dones})


def todo_done(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.complete = True
    todo.save()
    return redirect('todo_list')
