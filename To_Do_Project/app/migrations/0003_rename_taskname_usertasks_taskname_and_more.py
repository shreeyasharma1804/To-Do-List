# Generated by Django 5.1 on 2024-08-09 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_tasks_usertasks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usertasks',
            old_name='taskName',
            new_name='taskname',
        ),
        migrations.RenameField(
            model_name='usertasks',
            old_name='userName',
            new_name='username',
        ),
    ]
