# Generated by Django 5.0 on 2024-01-28 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_alter_education_id_alter_education_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='text',
            field=models.TextField(null=True),
        ),
    ]