# Generated by Django 5.0.2 on 2024-03-16 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='is_staff',
        ),
    ]
