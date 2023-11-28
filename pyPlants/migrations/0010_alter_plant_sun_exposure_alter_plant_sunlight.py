# Generated by Django 4.2.7 on 2023-11-28 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyPlants', '0009_plantuser_has_ai_enabled_alter_plant_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='sun_exposure',
            field=models.CharField(blank=True, choices=[('DIRECT_SUN', 'Direct Sun'), ('NO_DIRECT_SUN', 'No Direct Sun')], default='DIRECT_SUN', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='sunlight',
            field=models.CharField(blank=True, choices=[('LIGHT_EXPOSURE', 'Light Exposure'), ('PARTIAL_SHADE', 'Partial Shade'), ('SHADE', 'Shade')], default='LIGHT_EXPOSURE', max_length=20, null=True),
        ),
    ]
