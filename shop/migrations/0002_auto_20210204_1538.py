# Generated by Django 3.1.6 on 2021-02-04 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskbackgrounditem',
            name='colorcode_2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='taskbackgrounditem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/item/'),
        ),
    ]
