# Generated by Django 4.2.3 on 2023-07-14 22:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now, null=True),
        ),
        migrations.AddField(
            model_name='test',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]