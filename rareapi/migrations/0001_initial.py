# Generated by Django 4.1.3 on 2023-12-16 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=55)),
                ('last_name', models.CharField(max_length=55)),
                ('bio', models.CharField(max_length=55)),
                ('profile_image_url', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=55)),
                ('created_on', models.DateField()),
                ('uid', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('publication_date', models.DateField(auto_now=True)),
                ('image_url', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=100)),
                ('approved', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rareapi.category')),
                ('rare_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rareapi.user')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_on', models.DateField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rareapi.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rareapi.user')),
            ],
        ),
    ]
