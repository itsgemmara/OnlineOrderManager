from rest_framework import serializers

from .models import Cost, PeriodicCost, Income, PeriodicIncome
from .utils import period_choices_creator


class CostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cost
        fields = '__all__'


class PeriodicCostSerializer(serializers.ModelSerializer):
    REMINDER = (('one_hour', 'یک ساعت پیش از زمان پرداخت'),
                ('three_hour', 'سه ساعت پیش از زمان پرداخت'),
                ('one_day', 'یک روز پیش از زمان پرداخت'),
                ('three_day', 'سه روز پیش از زمان پرداخت'),
                ('one_week', 'یک هفته پیش از زمان پرداخت'),
                ('two_week', 'دو هفته پیش از زمان پرداخت'),
                ('one_month', 'یک ماه پیش از زمان پرداخت'),
                ('three_month', 'سه ماه پیش از زمان پرداخت'),
                ('six_month', 'شش ماه پیش از زمان پرداخت'),
                ('one_year', 'یک سال پیش از زمان پرداخت'),)
    reminder_of_Payment = serializers.MultipleChoiceField(choices=REMINDER)
    class Meta:
        model = PeriodicCost
        fields = '__all__'


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'


class PeriodicIncomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PeriodicIncome
        fields = '__all__'


class FilterSerializer(serializers.Serializer):
    search_key = serializers.CharField()


class PeriodFilterSerializer(serializers.Serializer):
    PERIOD = period_choices_creator()
    search_key = serializers.ChoiceField(choices=PERIOD)


class AmountFilterSerializer(serializers.Serializer):
    minimum = serializers.IntegerField(required=False, default=0)
    maximum = serializers.IntegerField(required=False, default=None)


class DateFilterSerializer(serializers.Serializer):
    from_date = serializers.DateTimeField(required=False, default=None)
    to_date = serializers.DateTimeField(required=False, default=None)


