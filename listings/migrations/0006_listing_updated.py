# Generated by Django 2.2.3 on 2019-07-08 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_listing_lifecycle'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
