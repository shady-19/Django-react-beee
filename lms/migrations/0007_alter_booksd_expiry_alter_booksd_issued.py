# Generated by Django 4.1.6 on 2023-02-15 06:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0006_alter_booksd_expiry_alter_booksd_issued'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksd',
            name='expiry',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 17, 11, 50, 48, 111356)),
        ),
        migrations.AlterField(
            model_name='booksd',
            name='issued',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 15, 11, 50, 48, 111356)),
        ),
    ]