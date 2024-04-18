# Generated by Django 5.0.2 on 2024-04-18 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processHandler', '0003_resume_profiletitle_alter_jobdescription_jdtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='profileTitle',
            field=models.TextField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='jobdescription',
            unique_together={('userId', 'jdTitle')},
        ),
        migrations.AlterUniqueTogether(
            name='resume',
            unique_together={('userId', 'profileTitle')},
        ),
    ]