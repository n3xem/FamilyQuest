# Generated by Django 3.1.6 on 2021-02-04 07:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0003_task_background_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completed_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='completed_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
