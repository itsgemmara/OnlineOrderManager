# Generated by Django 4.1 on 2022-12-14 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0021_m'),
    ]

    operations = [
        migrations.AlterField(
            model_name='m',
            name='time',
            field=models.TimeField(),
        ),
    ]