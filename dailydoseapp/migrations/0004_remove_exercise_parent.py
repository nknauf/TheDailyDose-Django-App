# Generated by Django 5.0.6 on 2024-07-02 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dailydoseapp', '0003_alter_exercise_parent_alter_musclegroup_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='parent',
        ),
    ]
