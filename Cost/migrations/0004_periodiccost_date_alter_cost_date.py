# Generated by Django 4.1 on 2022-10-01 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cost', '0003_remove_cost_reminder_of_payment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='periodiccost',
            name='date',
            field=models.DateTimeField(default='2022-09-27T12:34:00Z', verbose_name='تاریخ اولین پرداخت'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cost',
            name='date',
            field=models.DateTimeField(verbose_name='تاریخ'),
        ),
    ]