# Generated by Django 5.1.2 on 2025-01-17 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_batchcourseteacherassignment_section_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='batchcourseteacherassignment',
            name='Course_type',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
