# Generated by Django 3.2.7 on 2021-09-18 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('username', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('facebook', models.CharField(max_length=500)),
                ('instagram', models.CharField(max_length=500)),
                ('twitter', models.CharField(max_length=500)),
                ('linked_in', models.CharField(max_length=500)),
                ('youtube', models.CharField(max_length=500)),
                ('github', models.CharField(max_length=500)),
                ('gitlab', models.CharField(max_length=500)),
                ('website', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='userprofile',
            fields=[
                ('username', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=500)),
                ('DOB', models.DateField()),
                ('gender', models.BooleanField()),
                ('ac_type', models.BooleanField()),
            ],
        ),
    ]