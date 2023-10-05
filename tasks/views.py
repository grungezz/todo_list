from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from tasks.forms import TaskCreateForm
from tasks.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    context_object_name = 'tasks'
    paginate_by = 3

    @staticmethod
    def post(request, *args, **kwargs):
        task_id = request.POST.get('task_id')
        if task_id:
            task = get_object_or_404(Task, pk=task_id)
            task.is_done = not task.is_done
            task.save()
        return redirect(reverse_lazy('tasks:task-list'))


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy('tasks:task-list')


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:task-list")


class TagListView(generic.ListView):
    model = Tag
    context_object_name = 'tags'
    paginate_by = 9


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag-list")
