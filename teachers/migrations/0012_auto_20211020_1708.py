# Generated by Django 3.2.7 on 2021-10-20 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0011_auto_20211019_2136'),
    ]

    operations = [
        migrations.DeleteModel(
            name='assignments',
        ),
        migrations.DeleteModel(
            name='course',
        ),
        migrations.DeleteModel(
            name='exam',
        ),
        migrations.DeleteModel(
            name='project',
        ),
    ]
