# Generated by Django 4.1.7 on 2025-05-01 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingredients',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='likes',
        ),
        migrations.AddField(
            model_name='recipe',
            name='steps',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
