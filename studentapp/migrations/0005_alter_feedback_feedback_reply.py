# Generated by Django 3.2.10 on 2023-09-26 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0004_alter_staff_leave_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='feedback_reply',
            field=models.TextField(null=True),
        ),
    ]
