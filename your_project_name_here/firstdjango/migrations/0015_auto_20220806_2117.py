# Generated by Django 2.2.4 on 2022-08-07 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstdjango', '0014_auto_20220806_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tracks',
            name='link',
        ),
        migrations.AddField(
            model_name='tracks',
            name='extension',
            field=models.CharField(default='idk', max_length=255),
            preserve_default=False,
        ),
    ]
