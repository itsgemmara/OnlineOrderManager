from rest_framework.response import Response
from rest_framework import generics, mixins, views
from rest_framework.decorators import action
from rest_framework import viewsets
from  django.core.exceptions import ValidationError

from Filters import filters
from .serializers import *
from .models import PeriodicCost, Cost, Income, PeriodicIncome


class CostViewSet(viewsets.ModelViewSet):

    queryset = Cost.objects.all()
    serializer_class = CostSerializer

    def get_serializer_class(self):
        if self.action == 'name_search_filter' or self.action == 'description_search_filter':
            return FilterSerializer
        elif self.action == 'amount_search_filter':
            return AmountFilterSerializer
        elif self.action == 'date_search_filter':
            return DateFilterSerializer
        return CostSerializer

    @action(detail=False, methods=['post', ])
    def name_search_filter(self, r):
        response = filters.NameFilter(self.request.data, Cost)
        return Response(response.name_search_filter(), status=200)

    @action(detail=False, methods=['post', ])
    def description_search_filter(self, r):
        response = filters.description_search_filter(self.request.data, Cost)
        return Response(response, status=200)

    @action(detail=False, methods=['post', ])
    def amount_search_filter(self, r):
        response = filters.amount_search_filter(self.request.data, Cost)
        return Response(response, status=200)

    @action(detail=False, methods=['post', ])
    def date_search_filter(self, r):
        response = filters.date_search_filter(self.request.data, Cost)
        return Response(response, status=200)


class PeriodicCostViewSet(viewsets.ModelViewSet):

    queryset = PeriodicCost.objects.all()
    serializer_class = PeriodicCostSerializer

    def get_serializer_class(self):
        if self.action == 'name_search_filter' or self.action == 'description_search_filter':
            return PeriodicCostSerializer
        elif self.action == 'payment_period_search_filter':
            return PeriodFilterSerializer
        elif self.action == 'amount_search_filter':
            return AmountFilterSerializer
        elif self.action == 'date_search_filter':
            return DateFilterSerializer
        return PeriodicCostSerializer

    @action(detail=False, methods=['post', ])
    def payment_period_search_filter(self, r):
        serializer = PeriodFilterSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        search_key = serializer.validated_data["search_key"]
        filtering = Cost.objects.filter(payment_period=search_key)
        response = list()
        for i in filtering:
            response.append(i.pk)
        return Response(response, status=200)

