# Generated by Django 5.1.2 on 2025-01-16 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_teacher_id_alter_teacher_teacher_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='Is_Lab',
            field=models.BooleanField(default=False),
        ),
    ]
