# Generated by Django 3.2.9 on 2021-12-05 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_rename_cour_id_students_cour_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='skilsNcourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_id', models.CharField(max_length=255, unique=True)),
                ('skilset', models.JSONField()),
                ('courses', models.JSONField()),
            ],
        ),
    ]
