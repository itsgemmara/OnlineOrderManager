# Generated by Django 4.1 on 2022-09-21 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0008_pay_date_pay_products_id_pay_success_pay_total_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pay',
            old_name='products_id',
            new_name='products',
        ),
    ]
