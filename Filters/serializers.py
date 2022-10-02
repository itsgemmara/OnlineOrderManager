from rest_framework import serializers

from .utils import period_choices_creator


class TextSearchFilterSerializer(serializers.Serializer):
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


