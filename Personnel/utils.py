from Order.models import Category


def category_choices_creator():
    categories = Category.objects.all()
    choices = list()
    for i in categories:
        item = (f'{i.name}', f'{i.name}')
        choices.append(item)
    return tuple(choices)
