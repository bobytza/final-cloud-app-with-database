# Generated by Django 3.1.3 on 2023-07-27 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question',
            new_name='grade',
        ),
    ]
