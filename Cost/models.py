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
    reminder_of_payment = models.CharField('یادآور پرداخت', max_length=40)
    first_pay_date = models.DateTimeField('تاریخ اولین پرداخت', )
    is_finished = models.BooleanField('پایان یافته است', default=False)

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
    receive_period = models.CharField('دوره دریافت', max_length=20, choices=period_choices_creator())
    first_receive_date = models.DateTimeField('تاریخ اولین دریافت', )
    is_finished = models.BooleanField('پایان یافته است', default=False)

    def __str__(self):
        return self.name





