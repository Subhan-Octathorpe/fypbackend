# Generated by Django 5.1.2 on 2025-04-24 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_remove_teacher_archived_course_archived'),
    ]

    operations = [
        migrations.AddField(
            model_name='batchcourseteacherassignment',
            name='Archived',
            field=models.BooleanField(default=False),
        ),
    ]
