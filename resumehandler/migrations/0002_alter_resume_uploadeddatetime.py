# Generated by Django 5.0 on 2023-12-26 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumehandler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='uploadedDateTime',
            field=models.DateTimeField(),
        ),
    ]
