# Generated by Django 3.0.8 on 2020-07-29 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0010_event_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='fin',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='inicio',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
