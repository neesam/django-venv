# Generated by Django 2.2.4 on 2022-08-13 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstdjango', '0026_greatscene_jazz'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album', models.CharField(max_length=500)),
                ('artist', models.CharField(max_length=500)),
                ('image', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
