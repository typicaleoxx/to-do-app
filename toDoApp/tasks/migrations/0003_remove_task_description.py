# Generated by Django 5.0.1 on 2024-02-20 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='description',
        ),
    ]
