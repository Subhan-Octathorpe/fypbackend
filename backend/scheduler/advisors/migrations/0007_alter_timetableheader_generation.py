# Generated by Django 5.1.2 on 2025-03-11 02:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advisors', '0006_generation_timetableheader_generation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetableheader',
            name='Generation',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='advisors.generation'),
            preserve_default=False,
        ),
    ]
