from django.contrib import admin
from shop.models import TaskBackgroundItem, UsersTaskBackgroundItems

admin.site.register(TaskBackgroundItem)
admin.site.register(UsersTaskBackgroundItems)
