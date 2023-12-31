# Generated by Django 4.2.7 on 2023-11-28 13:05

from django.db import migrations, models
import pyPlants.utils


class Migration(migrations.Migration):

    dependencies = [
        ('pyPlants', '0007_plantuser_first_name_plantuser_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=pyPlants.utils.plant_pics_directory_path),
        ),
    ]
