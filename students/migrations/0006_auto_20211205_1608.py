# Generated by Django 3.2.9 on 2021-12-05 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_skilsncourse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skilsncourse',
            name='id',
        ),
        migrations.AlterField(
            model_name='skilsncourse',
            name='std_id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False, unique=True),
        ),
    ]
