# Generated by Django 5.0.6 on 2024-08-12 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dailydoseapp', '0005_remove_exercise_video_url_remove_musclegroup_parent_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userselection',
            name='equipment',
        ),
        migrations.RemoveField(
            model_name='userselection',
            name='muscle_groups',
        ),
        migrations.RemoveField(
            model_name='userselection',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserExerciseSelection',
        ),
        migrations.DeleteModel(
            name='UserSelection',
        ),
    ]
