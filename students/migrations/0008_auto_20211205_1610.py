# Generated by Django 3.2.9 on 2021-12-05 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_auto_20211205_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skilsncourse',
            name='courses',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='skilsncourse',
            name='skilset',
            field=models.JSONField(default=list),
        ),
    ]
