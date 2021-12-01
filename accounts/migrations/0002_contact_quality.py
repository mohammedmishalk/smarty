# Generated by Django 3.2.9 on 2021-11-22 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
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
            name='Quality',
            fields=[
                ('username', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('domain', models.CharField(max_length=50)),
                ('bio', models.CharField(max_length=255)),
                ('qu', models.CharField(max_length=1000)),
                ('ex', models.CharField(max_length=1000)),
            ],
        ),
    ]
