# Generated by Django 5.0 on 2024-01-28 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterModelTable(
            name='experience',
            table='dataextraction_experience',
        ),
    ]
