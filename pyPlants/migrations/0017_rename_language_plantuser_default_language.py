# Generated by Django 5.0 on 2024-01-05 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pyPlants', '0016_alter_plantuser_language'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plantuser',
            old_name='language',
            new_name='default_language',
        ),
    ]
