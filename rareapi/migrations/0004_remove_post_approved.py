# Generated by Django 4.1.3 on 2023-12-19 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0003_alter_comment_created_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='approved',
        ),
    ]
