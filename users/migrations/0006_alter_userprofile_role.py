# Generated by Django 5.0.2 on 2024-03-16 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_userprofile_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('1', 'Employee'), ('2', 'Employer')], default='1', max_length=255),
        ),
    ]
