# Generated by Django 4.1.6 on 2023-02-03 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('bid', models.AutoField(primary_key=True, serialize=False)),
                ('bname', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('about', models.CharField(max_length=1255)),
            ],
            options={
                'db_table': 'books',
            },
        ),
        migrations.CreateModel(
            name='librarian',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'librarian',
            },
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('uname', models.CharField(max_length=255)),
                ('uemail', models.CharField(max_length=255, unique=True)),
                ('upassword', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
