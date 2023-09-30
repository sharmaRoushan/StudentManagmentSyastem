# Generated by Django 3.2.10 on 2023-09-29 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0006_rename_craeted_at_feedback_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(default=0, null=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentapp.student')),
            ],
        ),
    ]