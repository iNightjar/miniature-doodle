# Generated by Django 4.1.2 on 2022-10-13 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_remove_movie_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie',
            field=models.CharField(max_length=30),
        ),
    ]
