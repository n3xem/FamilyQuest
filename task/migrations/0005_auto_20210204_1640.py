# Generated by Django 3.1.6 on 2021-02-04 07:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_userstaskbackgrounditems'),
        ('task', '0004_auto_20210204_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='background_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.taskbackgrounditem'),
        ),
    ]
