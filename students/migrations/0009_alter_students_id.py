# Generated by Django 3.2.9 on 2021-12-05 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_auto_20211205_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]