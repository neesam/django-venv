# Generated by Django 2.2.4 on 2022-09-23 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstdjango', '0036_melodiceng'),
    ]

    operations = [
        migrations.AlterField(
            model_name='melodiceng',
            name='artist',
            field=models.CharField(default='you a bitch', max_length=500),
        ),
        migrations.AlterField(
            model_name='melodiceng',
            name='title',
            field=models.CharField(default='you a bitch', max_length=500),
        ),
    ]
