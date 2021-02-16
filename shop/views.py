from shop.models import TaskBackgroundItem, UsersTaskBackgroundItems
from django.shortcuts import render
from django.views import generic

class IndexView(generic.ListView):
    model =  TaskBackgroundItem

    
def task_background_item_buy(request, pk):
    task_background_item = TaskBackgroundItem.objects.get(pk=pk)

    request.user.experience_point -= task_background_item.experience_point_cost
    request.user.save()
    new_users_task_background_items = UsersTaskBackgroundItems(user=request.user, item=task_background_item)
    new_users_task_background_items.save()

    context = { 'item': task_background_item }

    return render(request, 'shop/buy.html', context)