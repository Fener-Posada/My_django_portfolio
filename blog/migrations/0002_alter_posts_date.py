# Generated by Django 4.0.4 on 2022-05-18 19:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='Date',
            field=models.DateField(verbose_name=datetime.date.today),
        ),
    ]