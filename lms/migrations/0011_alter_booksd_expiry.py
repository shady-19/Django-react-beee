# Generated by Django 4.1.6 on 2023-02-15 12:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0010_alter_booksd_expiry_alter_booksd_issued'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksd',
            name='expiry',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 17, 17, 46, 38, 828756)),
        ),
    ]
