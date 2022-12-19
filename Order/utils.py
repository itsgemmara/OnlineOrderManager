import random
import string
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.fields import NOT_PROVIDED
from django.utils import timezone

from .models import Menu, Table, Category


def test_model_object_creator(model):
    fields = model._meta.get_fields()
    data = dict()
    red_list = list()
    for field in fields:
        if field.is_relation:
            if field.auto_created:
                continue
            value = test_model_object_creator(field.related_model)
        if field.name == 'id':
            continue
        if field.unique:
            qs = model.objects.all()
            red_list = list()
            for obj in qs:
                red_item = getattr(obj, f"{field.name}")
                red_list.append(red_item)
        if field.default != NOT_PROVIDED:
            data[field.name] = field.default
            continue
        elif type(field) == models.CharField:
            value = ''.join(random.choices(string.ascii_lowercase, k=field.max_length))
            while value in red_list:
                value = ''.join(random.choices(string.ascii_lowercase, k=field.max_length))
        elif type(field) == models.TextField:
            value = ''.join(random.choices(string.ascii_lowercase, k=10000))
        elif type(field) == models.IntegerField or type(field) == models.BigIntegerField:
            value = random.randint(1000000, 1000000000)
        elif type(field) == models.FloatField or type(field) == models.DecimalField:
            value = float(random.randint(1000000, 1000000000))
        elif type(field) == models.BooleanField:
            choice = random.randint(1, 2)
            value = True if choice == 1 else False
        elif type(field) == models.DateTimeField or type(field) == models.TimeField:
            value = timezone.now()
        data[field.name] = value
    obj = model.objects.create(**data)
    return obj


def choices_creator(model):
    menus = model.objects.all()
    choices = list()
    for i in menus:
        item = (f'{i.name}', f'{i.name}')
        choices.append(item)
    return tuple(choices)


def category_choices_creator():
    categories = Category.objects.all()
    choices = list()
    for i in categories:
        item = (f'{i.pk}', f'{i.name}')
        choices.append(item)
    return tuple(choices)


def table_choices_creator():
    tables = Table.objects.all()
    choices = list()
    for i in tables:
        item = (f'{i.name}', f'{i.name}')
        choices.append(item)
    return tuple(choices)


def create_factor(products):
    factor = dict()
    total_price = 0
    for i in products:
        try:
            product = Menu.objects.get(name=i)
        except:
            raise ValidationError(f'cant get menu obj with the given name = ({i})')
        price = product.price
        total_price += float(price)
        if product.name not in factor:
            count = 0
        else:
            elm = factor[product.name]
            count = elm['count']
        factor[product.name] = {'price': int(price) * (count + 1), 'count': count+1}
    return {'factor': factor, 'total_price': total_price}
