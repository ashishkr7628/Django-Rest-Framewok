# Generated by Django 5.1.1 on 2024-10-28 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='about',
            field=models.TextField(default=None, max_length=200),
        ),
    ]
