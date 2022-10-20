# Generated by Django 4.1 on 2022-09-07 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0002_remove_order_products_remove_order_total_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='عکس'),
        ),
        migrations.AlterField(
            model_name='order',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_ready',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='order',
            name='table',
            field=models.CharField(max_length=200),
        ),
    ]
