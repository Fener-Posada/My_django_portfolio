# Generated by Django 4.0.4 on 2022-06-08 14:50

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Short_Description', models.CharField(max_length=200)),
                ('Description', models.CharField(max_length=450)),
                ('Image_1', models.ImageField(upload_to='portfolio/images')),
                ('Image_2', models.ImageField(blank=True, upload_to='portfolio/images')),
                ('video', models.FileField(blank=True, upload_to='portfolio/images', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('Url', models.URLField(blank=True)),
                ('Categoria', models.CharField(max_length=250)),
                ('Date', models.DateField(verbose_name=datetime.date.today)),
            ],
        ),
    ]
