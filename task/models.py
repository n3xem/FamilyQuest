from django.db import models
from django.urls import reverse
from django.db.models.fields import BooleanField

class Task(models.Model):
    name = models.CharField(max_length=50)
    experience_point = models.IntegerField()
    client = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
    )
    completed_user = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        null=True,
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