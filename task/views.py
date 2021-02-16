from task.forms import TaskCreateForm
from django.db.models.deletion import SET_NULL
from django.db.models.lookups import IsNull
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin

def complete(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_completed = True
    task.completed_user = request.user
    task.save()

    request.user.experience_point += task.experience_point
    request.user.save()

    context = {
        'pk': pk ,
        'task': task,
    }
    return render(request, 'task/complete.html', context)

def incomplete(request, pk):
    task = Task.objects.get(pk=pk)
    
    task.completed_user.experience_point -= task.experience_point
    task.completed_user.save()

    task.is_completed = False
    task.completed_user = None
    task.save()


    context = {
        'pk': pk ,
        'task': task,
    }
    return render(request, 'task/complete.html', context)

class IndexView(generic.ListView):
    model = Task
    ordering = ['is_completed']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["login_user"] = self.request.user
        return context

class DetailView(generic.DetailView):
    model = Task

"""
class CreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Task
    fields = ['name', 'experience_point', 'is_show_child', 'background_item']
    login_url = '/login/'

    def form_valid(self, form):
        form.instance.client = self.request.user
        return super().form_valid(form)
"""

class CreateView(LoginRequiredMixin, generic.edit.CreateView):
    template_name = 'task/task_form.html'
    form_class = TaskCreateForm

    def form_valid(self,form):
        form.instance.client = self.request.user
        return super().form_valid(form)
    def get_form_kwargs(self):
        kwargs = super(CreateView, self).get_form_kwargs()
        kwargs['client'] = self.request.user
        return kwargs

class UpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Task
    fields = ['name', 'experience_point', 'is_show_child', 'background_item']
    login_url = '/login/'

    def form_valid(self, form):
        form.instance.client = self.request.user
        return super().form_valid(form)

class DeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Task
    success_url = reverse_lazy('task:index')
    login_url = '/login/'