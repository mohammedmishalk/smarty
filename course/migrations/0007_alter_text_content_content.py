# Generated by Django 3.2.9 on 2021-11-20 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_alter_regularclass_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text_content',
            name='content',
            field=models.CharField(max_length=10000),
        ),
    ]
