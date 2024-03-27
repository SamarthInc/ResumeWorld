# Generated by Django 5.0.2 on 2024-03-17 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_remove_userprofile_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='username',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='firstName',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='lastName',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
