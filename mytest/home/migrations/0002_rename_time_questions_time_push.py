# Generated by Django 4.2.1 on 2023-05-15 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions',
            old_name='time',
            new_name='time_push',
        ),
    ]