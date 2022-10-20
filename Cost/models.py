from django.db import models

from Order.models import Order
from .utils import period_choices_creator


class Cost(models.Model):
    name = models.CharField('نام', max_length=255)
    amount = models.IntegerField('مقدار به تومان', )
    description = models.TextField('توضیحات', null=True, blank=True)
    date = models.DateTimeField('تاریخ', )
    is_required = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class PeriodicCost(models.Model):
    name = models.CharField('نام', max_length=255)
    amount = models.IntegerField('مقدار به تومان', )
    description = models.TextField('توضیحات', null=True, blank=True)
    payment_period = models.CharField('دوره پرداخت', max_length=15, choices=period_choices_creator())
    is_required = models.BooleanField('ضروری است', default=True)
    reminder_of_Payment = models.CharField('یادآور پرداخت', max_length=40)
    first_pay_date = models.DateTimeField('تاریخ اولین پرداخت', )
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Income(models.Model):
    name = models.CharField('نام', max_length=255)
    amount = models.IntegerField('مقدار به تومان', )
    description = models.TextField('توضیحات', null=True, blank=True)
    date = models.DateTimeField('تاریخ', )

    def __str__(self):
        return self.name


class PeriodicIncome(models.Model):
    name = models.CharField('نام', max_length=255)
    amount = models.IntegerField('مقدار به تومان', )
    description = models.TextField('توضیحات', null=True, blank=True)
    payment_period = models.CharField('دوره پرداخت', max_length=20, choices=period_choices_creator())

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField('نام', max_length=255)
    UNIT = (('one_gr', 'یک گرم'),
            ('one_kg',  'یک کیلوگرم'),
            ('one_spoon', 'یک قاشق'),
            ('one_p', 'یک پیمانه'),
            ('other', 'دیگر'),)
    unit = models.CharField('واحد', max_length=20, choices=UNIT)
    unit_price = models.IntegerField('قیمت تقریبی هر واحد', )
    description = models.TextField('توضیحات', null=True, blank=True)

    def __str__(self):
        return self.name


class OrderCost(models.Model):
    order = models.OneToOneField(Order, on_delete=models.DO_NOTHING, verbose_name='نام سفارش')
    materials = models.TextField('مواد لازم', )
    total_price = models.IntegerField('قیمت کل', )
    description = models.TextField('توضیحات', null=True, blank=True)
