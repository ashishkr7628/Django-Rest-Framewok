# Generated by Django 5.1.1 on 2024-10-28 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_employee_about'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='about',
        ),
    ]
