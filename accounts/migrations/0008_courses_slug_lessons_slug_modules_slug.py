# Generated by Django 5.1.6 on 2025-03-06 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_courses_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='lessons',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='modules',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
