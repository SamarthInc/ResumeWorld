# Generated by Django 5.0 on 2024-01-28 13:43

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='resume.resume')),
                ('fullName', models.TextField()),
                ('phoneNumber', models.TextField()),
                ('email', models.TextField()),
                ('linkedinUrl', models.TextField()),
                ('githubUrl', models.TextField()),
                ('uploadedDateTime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
