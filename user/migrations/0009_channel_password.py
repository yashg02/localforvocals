# Generated by Django 3.1 on 2020-11-06 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20201106_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='password',
            field=models.CharField(default='pass1234', max_length=100, unique=False),
        ),
    ]
