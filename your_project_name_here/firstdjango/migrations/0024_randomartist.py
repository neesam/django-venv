# Generated by Django 2.2.4 on 2022-08-08 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstdjango', '0023_ryan_artist'),
    ]

    operations = [
        migrations.CreateModel(
            name='RandomArtist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=255)),
            ],
        ),
    ]