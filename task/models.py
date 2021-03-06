from django.db import models
from django.db.models.deletion import PROTECT, SET_NULL
from django.db.models.fields import BooleanField
from django.urls import reverse


class Task(models.Model):
    name = models.CharField(max_length=50)
    experience_point = models.IntegerField()
    background_item = models.ForeignKey(
        'shop.TaskBackgroundItem',
        default=1,
        on_delete=PROTECT
    )
    client = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
    )
    completed_user = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='completed_user'
    )
    is_show_child = models.BooleanField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('task:detail', kwargs={'pk': self.pk})
