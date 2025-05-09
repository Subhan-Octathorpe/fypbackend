# Generated by Django 5.1.2 on 2025-03-29 18:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_remove_advisor_password_remove_advisor_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advisor',
            name='deo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advisors', to='users.deo'),
        ),
        migrations.AlterField(
            model_name='advisor',
            name='faculty',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='advisor',
            name='seniority',
            field=models.CharField(blank=True, choices=[('professor', 'Professor'), ('associate_professor', 'Associate Professor'), ('assistant_professor', 'Assistant Professor'), ('lecturer', 'Lecturer'), ('it_manager_sr', 'IT Manager (Sr)'), ('it_manager_jr', 'IT Manager (Jr)')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='advisor',
            name='year',
            field=models.CharField(blank=True, choices=[('first', 'First'), ('second', 'Second'), ('third', 'Third'), ('fourth', 'Fourth')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='deo',
            name='department_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
