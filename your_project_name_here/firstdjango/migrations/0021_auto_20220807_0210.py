# Generated by Django 2.2.4 on 2022-08-07 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstdjango', '0020_randartist'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RandArtist',
            new_name='RandAlbum',
        ),
        migrations.RenameField(
            model_name='randalbum',
            old_name='artist',
            new_name='album',
        ),
    ]
