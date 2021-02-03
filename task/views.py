from django.urls import reverse_lazy
from django.views import generic
from .models import Task

class IndexView(generic.ListView):
    model = Task


