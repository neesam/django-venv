# Generated by Django 2.2.4 on 2022-09-23 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstdjango', '0035_criterion'),
    ]

    operations = [
        migrations.CreateModel(
            name='melodicEng',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('artist', models.CharField(max_length=500)),
            ],
        ),
    ]
