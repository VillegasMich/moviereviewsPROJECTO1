# Generated by Django 4.2.5 on 2023-09-25 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(default='movie/images/default.jpg', upload_to='movie/images/'),
        ),
    ]
