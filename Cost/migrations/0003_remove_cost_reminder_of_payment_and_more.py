# Generated by Django 4.1 on 2022-10-01 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cost', '0002_cost_is_required_cost_reminder_of_payment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cost',
            name='reminder_of_Payment',
        ),
        migrations.AddField(
            model_name='periodiccost',
            name='reminder_of_Payment',
            field=models.CharField(default='one_day', max_length=40, verbose_name='یادآور پرداخت'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cost',
            name='date',
            field=models.DateTimeField(verbose_name='تاریخ اولین پرداخت'),
        ),
        migrations.AlterField(
            model_name='periodiccost',
            name='is_required',
            field=models.BooleanField(default=True, verbose_name='ضروری است'),
        ),
    ]