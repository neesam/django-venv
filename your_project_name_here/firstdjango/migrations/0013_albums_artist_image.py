# Generated by Django 2.2.4 on 2022-08-07 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstdjango', '0012_auto_20220806_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='albums',
            name='artist_image',
            field=models.CharField(default='you a bitch', max_length=255),
            preserve_default=False,
        ),
    ]
