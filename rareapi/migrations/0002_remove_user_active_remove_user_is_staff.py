# Generated by Django 4.1.3 on 2023-12-14 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
    ]
