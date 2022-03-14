# Generated by Django 4.0.2 on 2022-03-14 20:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0006_assignment'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='confirmed',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='start',
            field=models.TimeField(default=datetime.time(23, 20, 12, 676382)),
        ),
    ]
