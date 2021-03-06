# Generated by Django 3.1.1 on 2020-09-21 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photographs', '0003_auto_20200921_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='aerialphoto',
            name='cancelled_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aerialphoto',
            name='description',
            field=models.TextField(default=0, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aerialphoto',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aerialphoto',
            name='small_description',
            field=models.TextField(default=0, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aerialphoto',
            name='specifications',
            field=models.TextField(default=0, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architecturalphoto',
            name='cancelled_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='architecturalphoto',
            name='description',
            field=models.TextField(default=0, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architecturalphoto',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='architecturalphoto',
            name='small_description',
            field=models.TextField(default=0, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architecturalphoto',
            name='specifications',
            field=models.TextField(default=0, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fashionphoto',
            name='cancelled_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fashionphoto',
            name='description',
            field=models.TextField(default=0, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fashionphoto',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fashionphoto',
            name='small_description',
            field=models.TextField(default=0, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fashionphoto',
            name='specifications',
            field=models.TextField(default=0, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fineartphoto',
            name='cancelled_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fineartphoto',
            name='description',
            field=models.TextField(default=0, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fineartphoto',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fineartphoto',
            name='small_description',
            field=models.TextField(default=0, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fineartphoto',
            name='specifications',
            field=models.TextField(default=0, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portraitphoto',
            name='cancelled_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='portraitphoto',
            name='description',
            field=models.TextField(default=0, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portraitphoto',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='portraitphoto',
            name='small_description',
            field=models.TextField(default=0, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portraitphoto',
            name='specifications',
            field=models.TextField(default=0, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sportsphoto',
            name='cancelled_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sportsphoto',
            name='description',
            field=models.TextField(default=0, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sportsphoto',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sportsphoto',
            name='small_description',
            field=models.TextField(default=0, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sportsphoto',
            name='specifications',
            field=models.TextField(default=0, max_length=2000),
            preserve_default=False,
        ),
    ]
