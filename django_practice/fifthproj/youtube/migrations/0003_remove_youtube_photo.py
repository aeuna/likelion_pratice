# Generated by Django 3.0.6 on 2020-07-13 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0002_auto_20200523_0341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='youtube',
            name='photo',
        ),
    ]
