# Generated by Django 2.2.1 on 2019-05-26 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pulogger', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datalogger',
            name='humidity_sensor_count',
        ),
        migrations.RemoveField(
            model_name='datalogger',
            name='temperature_sensor_count',
        ),
        migrations.AddField(
            model_name='datalogger',
            name='sensor_count',
            field=models.SmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='datalogger',
            name='description',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='datalogger',
            name='last_transmission',
            field=models.DateTimeField(null=True, verbose_name='last transmission received'),
        ),
        migrations.AlterField(
            model_name='datalogger',
            name='up_since',
            field=models.DateTimeField(null=True, verbose_name='uninterrupted since'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='description',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='sensormodel',
            name='description',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='sensormodel',
            name='has_humidity',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='sensormodel',
            name='has_temperature',
            field=models.BooleanField(default=False),
        ),
    ]
