# Generated by Django 3.0.6 on 2020-07-21 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200720_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='birthday',
            field=models.DateField(max_length=200),
        ),
        migrations.AlterField(
            model_name='customer',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
