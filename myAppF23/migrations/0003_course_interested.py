# Generated by Django 4.2.5 on 2023-11-08 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myAppF23', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='interested',
            field=models.PositiveIntegerField(default=0),
        ),
    ]