from django.db import models
from django.db.models.fields import IntegerField

class Item(models.Model):
    name = models.CharField(max_length=50)
    experience_point_cost = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class TaskBackgroundItem(Item):
    # 0 = colorbg, 1 = gradation, 2 = image
    type = IntegerField(default=0)

    colorcode = models.CharField(max_length=20, default='white')
    colorcode_2 = models.CharField(max_length=20, null=True)
    image = models.ImageField(upload_to='images/item/', null=True)
