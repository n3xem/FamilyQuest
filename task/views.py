from django.urls import reverse_lazy
from django.views import generic
from .models import Task

class IndexView(generic.ListView):
    model = Task

class DetailView(generic.DetailView):
    model = Task

class CreateView(generic.edit.CreateView):
    model = Task
    fields = '__all__' # 全てのカラムを指定