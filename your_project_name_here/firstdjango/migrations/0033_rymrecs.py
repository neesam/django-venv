# Generated by Django 2.2.4 on 2022-08-28 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstdjango', '0032_auto_20220827_2047'),
    ]

    operations = [
        migrations.CreateModel(
            name='RYMRecs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('artist', models.CharField(max_length=500)),
            ],
        ),
    ]
