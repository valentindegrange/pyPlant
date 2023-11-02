# Generated by Django 4.2.7 on 2023-11-02 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyPlants', '0003_notificationcenter_last_notification_sent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationcenter',
            name='last_notification_sent',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='fertilizer_season',
            field=models.CharField(blank=True, choices=[('Spring', 'Spring'), ('Autumn', 'Autumn')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='last_fertilized',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='last_repotted',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='last_watered',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='repotting_season',
            field=models.CharField(blank=True, choices=[('Spring', 'Spring'), ('Autumn', 'Autumn')], max_length=20, null=True),
        ),
    ]
