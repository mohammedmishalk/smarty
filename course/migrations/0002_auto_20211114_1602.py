# Generated by Django 3.2.9 on 2021-11-14 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img_content',
            name='id',
            field=models.CharField(max_length=15, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='text_content',
            name='id',
            field=models.CharField(max_length=15, primary_key=True, serialize=False, unique=True),
        ),
    ]
