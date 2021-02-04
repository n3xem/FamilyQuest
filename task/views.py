from django.urls import reverse_lazy
from django.views import generic
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(generic.ListView):
    model = Task
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["login_user"] = self.request.user
        return context

class DetailView(generic.DetailView):
    model = Task

class CreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Task
    fields = ['name', 'experience_point', 'is_show_child']
    login_url = '/login/'

    def form_valid(self, form):
        form.instance.client = self.request.user
        return super().form_valid(form)

class UpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Task
    fields = ['name', 'experience_point', 'is_show_child']
    login_url = '/login/'

    def form_valid(self, form):
        form.instance.client = self.request.user
        return super().form_valid(form)

class DeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Task
    success_url = reverse_lazy('task:index')
    login_url = '/login/'