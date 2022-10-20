from rest_framework import serializers

from .utils import table_choices_creator, menu_choices_creator, category_choices_creator
from .models import Order, Table, Pay


class TableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Table
        fields = ("name", "info")


class UpdateTableIsPayedSerializer(serializers.ModelSerializer):

    TABLE = table_choices_creator()
    table = serializers.ChoiceField(choices=TABLE)

    class Meta:
        model = Table
        fields = ("is_payed", 'table', )


class UpdateTableIsActiveSerializer(serializers.Serializer):

    TABLE = table_choices_creator()
    table = serializers.ChoiceField(choices=TABLE)

    CHOICES = (("ac", "activate"), ('de', 'deactivate'))
    choices = serializers.ChoiceField(choices=CHOICES)


class ChangeTableSerializer(serializers.Serializer):

    CHOICES = table_choices_creator()
    from_table = serializers.ChoiceField(choices=CHOICES)
    to = serializers.ChoiceField(choices=CHOICES)


class CreateOrderSerializer(serializers.ModelSerializer):

    MENU = menu_choices_creator()
    product = serializers.ChoiceField(choices=MENU)

    TABLE = table_choices_creator()
    table = serializers.ChoiceField(choices=TABLE)

    class Meta:
        model = Order
        fields = ("product", 'description', 'table')


class UpdateOrderDesSerializer(serializers.ModelSerializer):

    TABLE = table_choices_creator()
    table = serializers.ChoiceField(choices=TABLE)

    class Meta:
        model = Order
        fields = ('description', 'table')


class IsReadyOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('is_ready',)


class IsPayedOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('is_payed',)


class FilterOrderByTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pay
        fields = ('table', )


class SearchMenuFilterSerializer(serializers.Serializer):
    MENU = list(menu_choices_creator())
    MENU.append(('all', 'All'))
    source = serializers.ChoiceField(choices=tuple(MENU), required=False)
    search_key = serializers.CharField()


class OrderFilterSerializer(serializers.Serializer):
    MENU = list(menu_choices_creator())
    MENU.append(('all', 'All'))
    product = serializers.ChoiceField(choices=tuple(MENU))


class TableFilterSerializer(serializers.Serializer):
    TABLE = list(table_choices_creator())
    TABLE.append(('all', 'All Tables'))
    table = serializers.ChoiceField(choices=tuple(TABLE))


class IsReadyFilterSerializer(serializers.Serializer):
    CHOICES = ((True, 'is_ready'),
               (False, 'not_ready'),
               ('all', 'All'),)
    by = serializers.ChoiceField(choices=CHOICES)


class IsPayedFilterSerializer(serializers.Serializer):
    CHOICES = ((True, 'is_payed'),
               (False, 'not_payed'),
               ('all', 'All'),)
    by = serializers.ChoiceField(choices=CHOICES)


class DateFilterSerializer(serializers.Serializer):
    CHOICES = (('today', 'Today'),
               ('week', 'Past 7 days'),
               ('month', 'This month'),
               ('year', 'This year'),
               ('all', 'Any date'),)
    by = serializers.ChoiceField(choices=CHOICES)


class PaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pay
        fields = '__all__'


class UpdatePaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Pay
        fields = ('table', 'total_price', 'success')


class TableFactorSerializer(serializers.ModelSerializer):
    pay = serializers.BooleanField(default=True)
    class Meta:
        model = Pay
        fields = ('table', 'Pay')

class CategoryFilterSerializer(serializers.Serializer):
    CHOICES = category_choices_creator()
    by = serializers.MultipleChoiceField(choices=CHOICES)

