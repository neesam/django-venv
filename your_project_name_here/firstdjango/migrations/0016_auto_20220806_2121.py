# Generated by Django 2.2.4 on 2022-08-07 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstdjango', '0015_auto_20220806_2117'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tracks',
            old_name='name',
            new_name='track',
        ),
        migrations.AlterField(
            model_name='tracks',
            name='extension',
            field=models.CharField(default='idk', max_length=255),
        ),
    ]
