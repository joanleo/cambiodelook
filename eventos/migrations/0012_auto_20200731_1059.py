# Generated by Django 3.0.8 on 2020-07-31 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0011_auto_20200728_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='fin',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='inicio',
            field=models.TimeField(),
        ),
    ]
