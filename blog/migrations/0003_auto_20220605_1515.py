# Generated by Django 2.2.13 on 2022-06-05 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_posts_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
