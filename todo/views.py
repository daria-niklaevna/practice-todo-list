from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo.forms import TaskForm
from todo.models import Task, Tag


class ToDoListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "todo/task_list.html"
    paginate_by = 3


class ToDoCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")


class ToDoUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")
    template_name = "todo/task_form.html"


class ToDoDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-list")
    template_name = "todo/task_confirm_delete.html"


def change_progress_to_y(request, pk):
    task = Task.objects.get(id=pk)
    task.progress = "Y"
    task.save()
    return HttpResponseRedirect(reverse_lazy("todo:task-list"))


def change_progress_to_n(request, pk):
    task = Task.objects.get(id=pk)
    task.progress = "N"
    task.save()
    return HttpResponseRedirect(reverse_lazy("todo:task-list"))


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "todo/tag_list.html"
    paginate_by = 10


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")
    template_name = "todo/tag_form.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
    template_name = "todo/tag_confirm_delete.html"
