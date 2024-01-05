# Generated by Django 5.0 on 2024-01-05 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyPlants', '0015_plantuser_language_alter_plantuser_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantuser',
            name='language',
            field=models.CharField(choices=[('EN', 'English'), ('FR', 'French')], default='EN', max_length=2),
        ),
    ]