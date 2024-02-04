# Generated by Django 5.0.1 on 2024-02-04 08:35

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('configId', models.BigIntegerField()),
                ('keywordsScore', models.FloatField(null=True)),
                ('experienceScore', models.FloatField(null=True)),
                ('educationScore', models.FloatField(null=True)),
                ('finalScore', models.FloatField(null=True)),
                ('uploadedDateTime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'score',
            },
        ),
        migrations.CreateModel(
            name='ScoreConfig',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('keywordsConfig', models.IntegerField(null=True)),
                ('experienceConfig', models.IntegerField(null=True)),
                ('educationConfig', models.IntegerField(null=True)),
                ('uploadedDateTime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'score_config',
            },
        ),
    ]
