# Generated by Django 3.1.1 on 2020-09-21 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photographs', '0002_auto_20200921_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aerialphoto',
            name='cancelled_price',
        ),
        migrations.RemoveField(
            model_name='aerialphoto',
            name='description',
        ),
        migrations.RemoveField(
            model_name='aerialphoto',
            name='price',
        ),
        migrations.RemoveField(
            model_name='aerialphoto',
            name='small_description',
        ),
        migrations.RemoveField(
            model_name='aerialphoto',
            name='specifications',
        ),
        migrations.RemoveField(
            model_name='architecturalphoto',
            name='cancelled_price',
        ),
        migrations.RemoveField(
            model_name='architecturalphoto',
            name='description',
        ),
        migrations.RemoveField(
            model_name='architecturalphoto',
            name='price',
        ),
        migrations.RemoveField(
            model_name='architecturalphoto',
            name='small_description',
        ),
        migrations.RemoveField(
            model_name='architecturalphoto',
            name='specifications',
        ),
        migrations.RemoveField(
            model_name='fashionphoto',
            name='cancelled_price',
        ),
        migrations.RemoveField(
            model_name='fashionphoto',
            name='description',
        ),
        migrations.RemoveField(
            model_name='fashionphoto',
            name='price',
        ),
        migrations.RemoveField(
            model_name='fashionphoto',
            name='small_description',
        ),
        migrations.RemoveField(
            model_name='fashionphoto',
            name='specifications',
        ),
        migrations.RemoveField(
            model_name='fineartphoto',
            name='cancelled_price',
        ),
        migrations.RemoveField(
            model_name='fineartphoto',
            name='description',
        ),
        migrations.RemoveField(
            model_name='fineartphoto',
            name='price',
        ),
        migrations.RemoveField(
            model_name='fineartphoto',
            name='small_description',
        ),
        migrations.RemoveField(
            model_name='fineartphoto',
            name='specifications',
        ),
        migrations.RemoveField(
            model_name='portraitphoto',
            name='cancelled_price',
        ),
        migrations.RemoveField(
            model_name='portraitphoto',
            name='description',
        ),
        migrations.RemoveField(
            model_name='portraitphoto',
            name='price',
        ),
        migrations.RemoveField(
            model_name='portraitphoto',
            name='small_description',
        ),
        migrations.RemoveField(
            model_name='portraitphoto',
            name='specifications',
        ),
        migrations.RemoveField(
            model_name='sportsphoto',
            name='cancelled_price',
        ),
        migrations.RemoveField(
            model_name='sportsphoto',
            name='description',
        ),
        migrations.RemoveField(
            model_name='sportsphoto',
            name='price',
        ),
        migrations.RemoveField(
            model_name='sportsphoto',
            name='small_description',
        ),
        migrations.RemoveField(
            model_name='sportsphoto',
            name='specifications',
        ),
    ]
