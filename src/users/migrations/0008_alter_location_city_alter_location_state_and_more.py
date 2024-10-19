# Generated by Django 5.1.1 on 2024-10-19 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_location_city_alter_location_state_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='location',
            name='state',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='location',
            name='zip_code',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
