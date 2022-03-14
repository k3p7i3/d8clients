# Generated by Django 4.0.2 on 2022-03-14 18:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0010_alter_workday_end_alter_workday_start'),
        ('client', '0002_client_subscribes'),
        ('organization', '0005_service_name_alter_service_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date(2022, 3, 14))),
                ('start', models.TimeField(default=datetime.time(21, 22, 13, 162644))),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='client.client')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='staff.employee')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='organization.service')),
            ],
        ),
    ]
