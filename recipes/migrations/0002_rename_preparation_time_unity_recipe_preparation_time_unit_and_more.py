# Generated by Django 5.0.1 on 2024-02-19 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='preparation_time_unity',
            new_name='preparation_time_unit',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='servings_unity',
            new_name='servings_unit',
        ),
    ]
