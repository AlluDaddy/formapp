# Generated by Django 2.2.8 on 2021-10-31 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0002_auto_20211031_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='branch',
            field=models.CharField(default=' ', max_length=20),
        ),
        migrations.AddField(
            model_name='data',
            name='email',
            field=models.EmailField(default=' ', max_length=20),
        ),
    ]
