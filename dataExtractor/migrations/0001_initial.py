# Generated by Django 5.0 on 2024-01-28 09:19

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('uploadedDateTime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='JobDecription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('uploadedDateTime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('resumeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='dataExtractor.resume')),
                ('text', models.TextField()),
                ('uploadedDateTime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('resumeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='dataExtractor.resume')),
                ('text', models.TextField()),
                ('uploadedDateTime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('resumeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='dataExtractor.resume')),
                ('fullName', models.TextField()),
                ('phoneNumber', models.TextField()),
                ('email', models.TextField()),
                ('linkedinUrl', models.TextField()),
                ('githubUrl', models.TextField()),
                ('uploadedDateTime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]