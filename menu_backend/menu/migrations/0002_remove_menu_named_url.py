# Generated by Django 5.1.1 on 2024-09-12 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='named_url',
        ),
    ]
