# Generated by Django 4.1.6 on 2023-02-15 06:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0008_alter_booksd_expiry_alter_booksd_issued'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksd',
            name='expiry',
            field=models.DateField(default=datetime.datetime(2023, 3, 17, 11, 59, 54, 644772)),
        ),
        migrations.AlterField(
            model_name='booksd',
            name='issued',
            field=models.DateField(blank=True, default=datetime.date(2023, 2, 15)),
        ),
    ]
