# Generated by Django 3.1.6 on 2021-02-04 07:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_userstaskbackgrounditems'),
        ('task', '0005_auto_20210204_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='background_item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='shop.taskbackgrounditem'),
        ),
    ]
