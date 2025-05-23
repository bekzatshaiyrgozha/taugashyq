# Generated by Django 4.1.7 on 2025-05-01 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_remove_recipe_category_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='recipes.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
