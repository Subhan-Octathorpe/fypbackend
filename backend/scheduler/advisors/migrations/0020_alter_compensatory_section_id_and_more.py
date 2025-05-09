# Generated by Django 5.1.2 on 2025-03-29 17:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advisors', '0019_compensatory_day'),
        ('users', '0018_remove_advisor_password_remove_advisor_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compensatory',
            name='Section_ID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.section'),
        ),
        migrations.AlterField(
            model_name='coursepreferenceconstraints',
            name='Section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.section'),
        ),
    ]
