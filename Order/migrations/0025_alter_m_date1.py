# Generated by Django 4.1 on 2022-12-15 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0024_rename_date_m_date1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='m',
            name='date1',
            field=models.DateTimeField(),
        ),
    ]
