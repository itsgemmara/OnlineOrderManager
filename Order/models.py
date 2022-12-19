from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField('نام', max_length=1000)
    created_at = models.DateTimeField('تاریخ ثبت', auto_now=True)

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField('نام', max_length=1000)
    cat = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='دسته بندی')
    price = models.FloatField('قیمت')
    created_at = models.DateTimeField('تاریخ ثبت', auto_now=True)
    info = models.TextField('اطلاعات')
    image = models.ImageField('عکس', null=True, blank=True)

    def __str__(self):
        return self.name


class Table(models.Model):
    name = models.CharField('نام', max_length=1000, unique=True)
    created_at = models.DateTimeField('تاریخ ثبت', auto_now=True)
    info = models.TextField('اطلاعات')
    is_active = models.BooleanField('فعال', default=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.CharField('سفارش', max_length=2000)
    description = models.TextField('توضیحات', null=True, blank=True)
    table = models.CharField('میز', max_length=200)
    is_ready = models.BooleanField('آماده است', default=False)
    is_payed = models.BooleanField('پرداخت شده است', default=False)
    created_at = models.DateTimeField('تاریخ ثبت', auto_now=True)

    def __str__(self):
        return self.product


class Pay(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE, verbose_name='میز')
    total_price = models.CharField('قیمت کل', max_length=100)
    products = models.CharField('سفارشات', max_length=1000)
    date = models.DateTimeField('تاریخ ثبت', auto_now=True)
    success = models.BooleanField('پرداخت موفق', default=False)

    def __str__(self):
        return self.id


class Material(models.Model):
    name = models.CharField('نام', max_length=255, unique=True)
    UNIT = (('one_gr', 'گرم'),
            ('one_kg',  'کیلوگرم'),
            ('one_spoon', 'قاشق'),
            ('one_p', 'پیمانه'),
            ('other', 'دیگر'),)
    unit = models.CharField('واحد', max_length=20, choices=UNIT)
    unit_price = models.FloatField('قیمت هر واحد به تومان', null=True, blank=True)
    description = models.TextField('توضیحات', null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    order = models.OneToOneField(Menu, on_delete=models.DO_NOTHING, verbose_name='نام سفارش')
    materials = models.TextField('مواد لازم', )
    description = models.TextField('طرز تهیه', null=True, blank=True)

#
# class M(models.Model):
#     name = models.CharField(max_length=10000, unique=True)
#     text = models.TextField()
#     bool2 = models.BooleanField()
#     date1 = models.DateTimeField(auto_created=True)
#     time = models.TimeField()
#
