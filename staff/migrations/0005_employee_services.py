# Generated by Django 4.0.2 on 2022-03-13 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_service'),
        ('staff', '0004_admin_confirmed_employee_confirmed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='services',
            field=models.ManyToManyField(blank=True, related_name='employees', to='organization.Service'),
        ),
    ]
