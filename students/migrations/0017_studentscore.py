# Generated by Django 3.2.9 on 2022-01-10 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0016_auto_20211230_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stud_id', models.CharField(max_length=255)),
                ('course_id', models.CharField(max_length=255)),
                ('exam', models.JSONField(default=list)),
                ('project', models.FileField(upload_to='project/')),
                ('assignment', models.JSONField(default=list)),
            ],
        ),
    ]
