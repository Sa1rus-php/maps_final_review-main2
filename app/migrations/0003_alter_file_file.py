# Generated by Django 4.2.1 on 2023-05-31 15:51

from django.db import migrations, models
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_file_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FilePathField(allow_folders=pathlib.PurePosixPath('/home/anton/PycharmProjects/Map_Parser/media')),
        ),
    ]
