# Generated by Django 2.2.2 on 2019-06-14 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_auto_20190614_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='listing',
            name='city',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='listing',
            name='delivery',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='listing',
            name='state',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='listing',
            name='zipcode',
            field=models.CharField(max_length=255),
        ),
    ]
