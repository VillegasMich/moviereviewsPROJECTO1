# Generated by Django 4.2.5 on 2023-09-25 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_alter_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(default='media/movie/images/default.jpg', upload_to='media/movie/images/'),
        ),
    ]
