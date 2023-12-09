# Generated by Django 4.1 on 2023-11-25 18:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='BookingDate',
            field=models.DateField(default=datetime.date(2023, 11, 25)),
        ),
        migrations.AddField(
            model_name='booking',
            name='No_of_guests',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='booking',
            name='ID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='menu',
            name='ID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
