# Generated by Django 3.2.9 on 2021-11-21 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
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
