from django.core.exceptions import ValidationError


from .models import Menu, Table, Category


def menu_choices_creator():
    menus = Menu.objects.all()
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
        total_price += int(price)
        if product.name not in factor:
            count = 0
        else:
            elm = factor[product.name]
            count = elm['count']
        factor[product.name] = {'price': int(price) * (count + 1), 'count': count+1}
    return {'factor': factor, 'total_price': total_price}
