# Generated by Django 5.0.7 on 2024-09-12 13:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="category",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="recipes.category",
            ),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="cover",
            field=models.ImageField(
                blank=True, default="", upload_to="recipes/covers/%Y/%m/%d/"
            ),
        ),
    ]
