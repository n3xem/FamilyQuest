from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),
  path('taskbg/<int:pk>/buy', views.task_background_item_buy, name='taskbg_buy'),
  path('taskbg/<int:pk>/buy-fail', views.task_background_buy_fail, name='taskbg_buy_fail'),
]
