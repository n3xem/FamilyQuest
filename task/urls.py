from django.urls import path
from . import views

app_name = 'task'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.UpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
    path('<int:pk>/complete/', views.complete, name='complete'),
    path('<int:pk>/incomplete/', views.incomplete, name='incomplete'),
]
