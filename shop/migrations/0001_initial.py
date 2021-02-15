# Generated by Django 3.1.6 on 2021-02-04 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskBackgroundItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('experience_point_cost', models.IntegerField(default=0)),
                ('type', models.IntegerField(default=0)),
                ('colorcode', models.CharField(default='white', max_length=20)),
                ('colorcode_2', models.CharField(max_length=20, null=True)),
                ('image', models.ImageField(null=True, upload_to='images/item/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]