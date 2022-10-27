from rest_framework.response import Response
from rest_framework import generics, mixins, views
from rest_framework.decorators import action
from rest_framework import viewsets
from django.core.exceptions import ValidationError

from Filters import filters, serializers as filter_serializers
from .serializers import *
from .models import PeriodicCost, Cost, Income, PeriodicIncome


class CostViewSet(viewsets.ModelViewSet):

    queryset = Cost.objects.all()
    serializer_class = CostSerializer

    def get_serializer_class(self):
        if self.action == 'name_search_filter' or self.action == 'description_search_filter':
            return filter_serializers.TextSearchFilterSerializer
        elif self.action == 'amount_search_filter':
            return filter_serializers.AmountFilterSerializer
        elif self.action == 'date_search_filter':
            return DateFilterSerializer
        elif self.action == 'is_required_search_filter':
            return filter_serializers.BooleanFilterSerializer
        return CostSerializer

    @action(detail=False, methods=['post', ])
    def name_search_filter(self, r):
        response = filters.Filter(self.request.data, Cost, 'name')
        return Response(response.char_field(), status=200)

    @action(detail=False, methods=['post', ])
    def description_search_filter(self, r):
        response = filters.Filter(self.request.data, Cost, 'description')
        return Response(response.char_field(), status=200)

    @action(detail=False, methods=['post', ])
    def amount_search_filter(self, r):
        response = filters.Filter(self.request.data, Cost, 'amount')
        return Response(response.integer_field_filter(), status=200)

    @action(detail=False, methods=['post', ])
    def date_search_filter(self, r):
        response = filters.Filter(self.request.data, Cost, 'date')
        return Response(response.interval_date_field_filter(), status=200)

    @action(detail=False, methods=['post', ])
    def is_required_search_filter(self, r):
        response = filters.Filter(self.request.data, Cost, 'is_required')
        return Response(response.bool_field(), status=200)


class PeriodicCostViewSet(viewsets.ModelViewSet):

    queryset = PeriodicCost.objects.all()
    serializer_class = PeriodicCostSerializer

    def get_serializer_class(self):
        if self.action == 'name_search_filter' or self.action == 'description_search_filter':
            return filter_serializers.TextSearchFilterSerializer
        elif self.action == 'payment_period_search_filter':
            return PeriodFilterSerializer
        elif self.action == 'amount_search_filter':
            return filter_serializers.AmountFilterSerializer
        elif self.action == 'create':
            return PeriodicCostSerializer
        elif self.action == 'reminder_of_payment_search_filter':
            return ReminderFilterSerializer
        elif self.action == 'date_search_filter':
            return filter_serializers.DateFilterSerializer
        elif self.action == 'is_finished_search_filter':
            return filter_serializers.BooleanFilterSerializer
        return PeriodicCostListSerializer

    @action(detail=False, methods=['post', ])
    def name_search_filter(self, r):
        response = filters.Filter(self.request.data, PeriodicCost, 'name')
        return Response(response.char_field(), status=200)

    @action(detail=False, methods=['post', ])
    def description_search_filter(self, r):
        response = filters.Filter(self.request.data, PeriodicCost, 'description')
        return Response(response.char_field(), status=200)

    @action(detail=False, methods=['post', ])
    def amount_search_filter(self, r):
        response = filters.Filter(self.request.data, PeriodicCost, 'amount')
        return Response(response.integer_field_filter(), status=200)

    @action(detail=False, methods=['post', ])
    def is_required_search_filter(self, r):
        response = filters.Filter(self.request.data, PeriodicCost, 'is_required')
        return Response(response.bool_field(), status=200)

    @action(detail=False, methods=['post', ])
    def payment_period_search_filter(self, r):
        response = filters.Filter(self.request.data, PeriodicCost, 'payment_period')
        return Response(response.choice_field(PeriodFilterSerializer, ['filter_by']), status=200)

    @action(detail=False, methods=['post', ])
    def reminder_of_payment_search_filter(self, r):
        response = filters.Filter(self.request.data, PeriodicCost, 'reminder_of_payment')
        return Response(response.choice_field(ReminderFilterSerializer, ['filter_by']), status=200)

    @action(detail=False, methods=['post', ])
    def date_search_filter(self, r):
        response = filters.Filter(self.request.data, PeriodicCost, 'first_pay_date')
        return Response(response.date_field_filter(), status=200)

    @action(detail=False, methods=['post', ])
    def is_finished_search_filter(self, r):
        response = filters.Filter(self.request.data, PeriodicCost, 'is_finished')
        return Response(response.bool_field(), status=200)


class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

    def get_serializer_class(self):
        if self.action == 'name_search_filter' or self.action == 'description_search_filter':
            return filter_serializers.TextSearchFilterSerializer
        elif self.action == 'amount_search_filter':
            return filter_serializers.AmountFilterSerializer
        elif self.action == 'date_search_filter':
            return filter_serializers.IntervalDateFilterSerializer
        return IncomeSerializer

    @action(detail=False, methods=['post', ])
    def name_search_filter(self, r):
        response = filters.Filter(self.request.data, Income, 'name')
        return Response(response.char_field(), status=200)

    @action(detail=False, methods=['post', ])
    def description_search_filter(self, r):
        response = filters.Filter(self.request.data, Income, 'description')
        return Response(response.char_field(), status=200)

    @action(detail=False, methods=['post', ])
    def amount_search_filter(self, r):
        response = filters.Filter(self.request.data, Income, 'amount')
        return Response(response.integer_field_filter(), status=200)

    @action(detail=False, methods=['post', ])
    def date_search_filter(self, r):
        response = filters.Filter(self.request.data, Cost, 'date')
        return Response(response.interval_date_field_filter(), status=200)


class PeriodicIncomeViewSet(viewsets.ModelViewSet):

    queryset = PeriodicIncome.objects.all()

    def get_serializer_class(self):
        if self.action == 'name_search_filter' or self.action == 'description_search_filter':
            return filter_serializers.TextSearchFilterSerializer
        elif self.action == 'receive_period_search_filter':
            return PeriodFilterSerializer
        elif self.action == 'amount_search_filter':
            return filter_serializers.AmountFilterSerializer
        elif self.action == 'date_search_filter':
            return filter_serializers.DateFilterSerializer
        elif self.action == 'is_finished_search_filter':
            return filter_serializers.BooleanFilterSerializer
        return PeriodicIncomeSerializer

    @action(detail=False, methods=['post', ])
    def name_search_filter(self, r):
        response = filters.Filter(self.request.data, PeriodicIncome, 'name')
        return Response(response.char_field(), status=200)

    @action(detail=False, methods=['post', ])
    def description_search_filter(self, r):
        response = filters.Filter(self.request.data, PeriodicIncome, 'description')
        return Response(response.char_field(), status=200)

    @action(detail=False, methods=['post', ])
    def amount_search_filter(self, r):
        response = filters.Filter(self.request.data, PeriodicIncome, 'amount')
        return Response(response.integer_field_filter(), status=200)

    @action(detail=False, methods=['post', ])
    def receive_period_search_filter(self, r):
        response = filters.Filter(self.request.data, PeriodicIncome, 'receive_period')
        return Response(response.choice_field(PeriodFilterSerializer, ['filter_by']), status=200)

    @action(detail=False, methods=['post', ])
    def date_search_filter(self, r):
        response = filters.Filter(self.request.data, PeriodicIncome, 'first_receive_date')
        return Response(response.date_field_filter(), status=200)

    @action(detail=False, methods=['post', ])
    def is_finished_search_filter(self, r):
        response = filters.Filter(self.request.data, PeriodicIncome, 'is_finished')
        return Response(response.bool_field(), status=200)

