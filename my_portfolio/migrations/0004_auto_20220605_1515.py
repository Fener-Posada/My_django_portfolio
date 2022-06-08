# Generated by Django 2.2.13 on 2022-06-05 20:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_portfolio', '0003_projects_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='video',
            field=models.FileField(null=True, upload_to='portfolio/images', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])]),
        ),
    ]