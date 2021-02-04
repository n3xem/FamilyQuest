from shop.models import TaskBackgroundItem
from django.shortcuts import render
from django.views import generic

class IndexView(generic.ListView):
    model =  TaskBackgroundItem
    