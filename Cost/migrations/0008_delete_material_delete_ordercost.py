# Generated by Django 4.1 on 2022-10-16 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cost', '0007_remove_periodicincome_payment_period_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Material',
        ),
        migrations.DeleteModel(
            name='OrderCost',
        ),
    ]
