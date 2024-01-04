# Generated by Django 5.0 on 2024-01-04 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyPlants', '0013_plant_needs_care'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='plantuser',
            name='has_ai_enabled',
            field=models.BooleanField(default=False, help_text='Whether the user has AI features enabled or not'),
        ),
    ]
