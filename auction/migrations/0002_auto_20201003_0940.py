# Generated by Django 3.1.2 on 2020-10-03 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auction',
            old_name='price',
            new_name='bid',
        ),
    ]
