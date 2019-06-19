# Generated by Django 2.2.2 on 2019-06-14 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_auto_20190614_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='address',
            field=models.CharField(default='ADD', max_length=255),
        ),
        migrations.AddField(
            model_name='listing',
            name='city',
            field=models.CharField(default='ADD', max_length=255),
        ),
        migrations.AddField(
            model_name='listing',
            name='delivery',
            field=models.CharField(default='ADD', max_length=255),
        ),
        migrations.AddField(
            model_name='listing',
            name='state',
            field=models.CharField(default='ADD', max_length=255),
        ),
        migrations.AddField(
            model_name='listing',
            name='zipcode',
            field=models.CharField(default='ADD', max_length=255),
        ),
    ]
