# Generated by Django 4.0.3 on 2022-03-15 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='recipient',
        ),
    ]