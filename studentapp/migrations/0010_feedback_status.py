# Generated by Django 3.2.10 on 2023-09-30 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0009_student_feedback_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
