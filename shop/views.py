from django.shortcuts import redirect, render
from shop.models import TaskBackgroundItem, UsersTaskBackgroundItems


def index_view(request):
    bought_item_pks = list(
        UsersTaskBackgroundItems
        .objects
        .filter(user__pk=request.user.pk)
        .values_list('item', flat=True)
    )

    bought_items = TaskBackgroundItem.objects.filter(pk__in=bought_item_pks)
    not_bought_items = TaskBackgroundItem.objects.exclude(
        pk__in=bought_item_pks)

    context = {
        'object_list': not_bought_items,
        'bought_items': bought_items,
    }
    return render(request, 'shop/taskbackgrounditem_list.html', context)


def task_background_item_buy(request, pk):
    task_background_item = TaskBackgroundItem.objects.get(pk=pk)

    if request.user.experience_point - task_background_item.experience_point_cost < 0:
        return redirect('shop:taskbg_buy_fail', pk=pk)

    request.user.experience_point -= task_background_item.experience_point_cost
    request.user.save()
    new_users_task_background_items = UsersTaskBackgroundItems(user=request.user,
                                                               item=task_background_item)
    new_users_task_background_items.save()

    context = {
        'item': task_background_item
    }
    return render(request, 'shop/buy.html', context)


def task_background_buy_fail(request, pk):
    task_background_item = TaskBackgroundItem.objects.get(pk=pk)

    context = {
        'item': task_background_item,
        'diff': request.user.experience_point - task_background_item.experience_point_cost,
    }
    return render(request, 'shop/buy-fail.html', context)
