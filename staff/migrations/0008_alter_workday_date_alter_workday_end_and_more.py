# Generated by Django 4.0.2 on 2022-03-14 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0007_alter_workday_end_alter_workday_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workday',
            name='date',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='workday',
            name='end',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='workday',
            name='start',
            field=models.CharField(default='', max_length=5),
        ),
    ]
