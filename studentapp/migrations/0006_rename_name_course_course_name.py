# Generated by Django 3.2.10 on 2023-09-06 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0005_rename_course_name_course_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='name',
            new_name='course_name',
        ),
    ]
