# Generated by Django 4.1.7 on 2025-05-01 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_alter_recipe_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='category',
            new_name='category_id',
        ),
    ]
