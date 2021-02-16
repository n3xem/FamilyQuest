from django import forms
from .models import Task
from icecream import ic
from shop.models import TaskBackgroundItem, UsersTaskBackgroundItems

class TaskCreateForm(forms.ModelForm):
    class Meta:
       model = Task
       fields = ['name', 'experience_point', 'is_show_child', 'background_item']

    def __init__(self, *args, **kwargs):
      user = kwargs.pop('client')
      super(TaskCreateForm, self).__init__(*args, **kwargs)
      usersitems = UsersTaskBackgroundItems.objects.filter(user=user).values('item_id')
      pk_list = [ i['item_id'] for i in usersitems]
      self.fields['background_item'].queryset = TaskBackgroundItem.objects.filter(pk__in=pk_list)