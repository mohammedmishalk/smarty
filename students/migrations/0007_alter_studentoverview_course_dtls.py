# Generated by Django 3.2.9 on 2021-11-21 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_alter_studentoverview_course_dtls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentoverview',
            name='course_dtls',
            field=models.JSONField(default={}),
        ),
    ]
