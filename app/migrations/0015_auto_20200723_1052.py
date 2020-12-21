# Generated by Django 3.0.6 on 2020-07-23 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20200722_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Otrher')], max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='sexo',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Otrher')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='profesional',
            field=models.ManyToManyField(blank=True, null=True, to='app.Profesional'),
        ),
    ]
