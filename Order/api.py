from rest_framework.response import Response
from rest_framework import generics, mixins, views
from rest_framework.decorators import action
from rest_framework import viewsets
from django.core.exceptions import ValidationError

from .serializers import *
from .models import Order, Table, Menu, Category, Material, Product
from .utils import create_factor, test_model_object_creator
from Filters import filters, utils, serializers as filter_serializers


class TableViewSet(viewsets.ModelViewSet):

    """
    General ViewSet description

    list: List tables

    retrieve: Retrieve table

    update: Update table

    create: Create table

    partial_update: Patch table

    destroy: delete table

    change_table_is_active: change tables is_active boolean.

    """

    queryset = Table.objects.all()
    serializer_class = TableSerializer

    def get_serializer_class(self):
        if self.action == 'set_table_is_payed':
            return UpdateTableIsPayedSerializer
        if self.action == 'change_table_is_active':
            return UpdateTableIsActiveSerializer
        elif self.action == 'change_table':
            return ChangeTableSerializer
        elif self.action == 'create_table_factor':
            return TableFactorSerializer
        return TableSerializer

    @action(detail=False, methods=['post', ])
    def change_table_is_active(self, r):
        serializer = UpdateTableIsActiveSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        key = serializer.validated_data["choices"]
        table = serializer.validated_data["table"]
        try:
            table = Table.objects.get(name=table)
        except:
            raise ValidationError(f'cant get obj with the given table: ({table})')
        if key == 'ac':
            try:
                table.is_active = True
                table.save()
            except:
                raise ValidationError('cant change is_active field to true.')
        elif key == 'de':
            try:
                table.is_active = False
                table.save()
            except:
                raise ValidationError('cant change is_active field to false.')
        return Response('done', status=200)

    @action(detail=False, methods=['post', ])
    def change_table(self, r):
        serializer = ChangeTableSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        _from_table = serializer.validated_data["from_table"]
        _to = serializer.validated_data["to"]
        try:
            from_table = Table.objects.get(name=_from_table)
            to = Table.objects.get(name=_to)
        except:
            raise ValidationError('cant get table obj')
        active_orders = Order.objects.filter(is_payed=False, is_ready=False, table=from_table)
        for order in active_orders:
            order.table = to
            order.save()
        return Response('done', status=200)

    @action(detail=False, methods=['post', ])
    def create_table_factor(self, r):
        serializer = TableFactorSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        table = serializer.validated_data["table"]
        _products = Order.objects.filter(table=table, is_active=False)
        products = list()
        for i in _products:
            products.append(i.product)
        factor = create_factor(products)
        print(factor)
        return Response(factor, status=200)

    @action(detail=False, methods=['get', ])
    def get_active_tables(self, r):
        test_model_object_creator(Menu)
        try:
            active_tables = Table.objects.filter(is_active=True)
        except:
            raise ValidationError('cant filter table objects')
        response = list()
        for i in active_tables:
            response.append(i.name)
        return Response(response, status=200)


class OrderViewSet(viewsets.ModelViewSet):

    """
    General ViewSet description

    list: List order

    retrieve: Retrieve order

    update: Update order

    create: Create order

    partial_update: Patch order

    """

    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.action == 'set_order_is_payed':
            return UpdateTableIsPayedSerializer
        elif self.action == 'set_order_is_ready':
            return IsReadyOrderSerializer
        elif self.action == 'update' or self.action == 'partial_update':
            return UpdateOrderDesSerializer
        elif self.action == 'description_search_filter':
            return SearchMenuFilterSerializer
        elif self.action == 'product_search_filter':
            return OrderFilterSerializer
        elif self.action == 'is_ready_search_filter':
            return filter_serializers.BooleanFilterSerializer
        elif self.action == 'is_payed_search_filter':
            return filter_serializers.BooleanFilterSerializer
        elif self.action == 'table_search_filter':
            return TableFilterSerializer
        elif self.action == 'category_search_filter':
            return CategoryFilterSerializer
        return CreateOrderSerializer

    @action(detail=True, methods=['post', ])
    def set_order_is_payed(self, r, pk):
        serializer = UpdateTableIsPayedSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        is_payed = serializer.validated_data["is_payed"]
        if is_payed:
            try:
                order = Order.objects.get(pk=pk)
            except:
                raise ValidationError('cant get order obj')
            if order.is_payed:
                raise ValidationError('order is already payed.')
            try:
                order.is_payed = True
                order.save()
            except:
                raise ValidationError('cant change is_payed in order to true')
        else:
            raise ValidationError('selecting the box is required')
        return Response('done', status=200)

    @action(detail=True, methods=['post', ])
    def set_order_is_ready(self, r, pk):
        serializer = IsReadyOrderSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        is_ready = serializer.validated_data["is_ready"]
        if is_ready:
            try:
                order = Order.objects.get(pk=pk)
            except:
                raise ValidationError('cant get order obj')
            try:
                order.is_ready = True
                order.save()
            except:
                raise ValidationError('cant change is_ready in order to true')
        return Response('done', status=200)

    @action(detail=False, methods=['post', ])
    def description_search_filter(self, r):
        custom_filter = filters.BaseFilter(data=self.request.data, model=Order,
                                           serializer_fields=['source', 'search_key'],
                                           serializer=SearchMenuFilterSerializer)
        parameters = custom_filter.create_parameters()
        if parameters['source'] != 'all':
            filter_dict = {'product': parameters['source'], 'description__contains': parameters['search_key']}
        else:
            filter_dict = {'description__contains': parameters['search_key']}
        response = custom_filter.filter(filter_dict)
        return Response(response, status=200)

    @action(detail=False, methods=['post', ])
    def product_search_filter(self, r):
        custom_filter = filters.BaseFilter(data=self.request.data, model=Order,
                                           serializer_fields=["product"],
                                           serializer=OrderFilterSerializer)
        parameters = custom_filter.create_parameters()
        if parameters['product'] != 'all':
            filter_dict = {'product': parameters['product']}
            response = custom_filter.filter(filter_dict)
        else:
            filtering = Order.objects.all()
            response = utils.pk_response_creator(filtering)
        return Response(response, status=200)

    @action(detail=False, methods=['post', ])
    def table_search_filter(self, r):
        response = filters.Filter(self.request.data, Order, 'table')
        return Response(response.choice_field(TableFilterSerializer, ['table']), status=200)

    @action(detail=False, methods=['post', ])
    def is_ready_search_filter(self, r):
        response = filters.Filter(self.request.data, Order, 'is_ready')
        return Response(response.bool_field(), status=200)

    @action(detail=False, methods=['post', ])
    def is_payed_search_filter(self, r):
        response = filters.Filter(self.request.data, Order, 'is_payed')
        return Response(response.bool_field(), status=200)

    @action(detail=False, methods=['post', ])
    def category_search_filter(self, r):
        custom_filter = filters.BaseFilter(data=self.request.data, model=Order,
                                           serializer_fields=["by"],
                                           serializer=CategoryFilterSerializer)
        parameters = custom_filter.create_parameters()
        response = list()
        for category in parameters['by']:
            category = Category.objects.get(pk=int(category))
            menus = Menu.objects.filter(cat=category)
            for menu in menus:
                orders = Order.objects.filter(product=menu.name)
                for order in orders:
                    response.append(order.pk)
        return Response(response, status=200)


class PayViewSet(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    """
    General ViewSet description

    list: List pay

    retrieve: Retrieve pay

    update: Update pay

    create: Create pay

    partial_update: Patch pay

    """

    queryset = Pay.objects.all()
    serializer_class = PaySerializer

    def get_serializer_class(self):
        if self.action == 'create_table_factor':
            return TableFactorSerializer
        elif self.action == 'set_order_is_ready':
            return IsReadyOrderSerializer
        elif self.action == 'update' or self.action == 'partial_update':
            return UpdatePaySerializer
        elif self.action == 'description_search_filter':
            return SearchMenuFilterSerializer
        return PaySerializer

    @action(detail=False, methods=['post', ])
    def create_table_factor(self, r):
        serializer = TableFactorSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        table = serializer.validated_data["table"]
        try:
            table = Table.objects.get(name=table)
        except:
            raise ValidationError(f'Cant get obj with the given table: ({table})')
        _products = Order.objects.filter(table=table, is_active=False)
        products = list()
        for i in _products:
            products.append(i.product)
        factor = create_factor(products)
        return Response(factor, status=200)

    @action(detail=False, methods=['post', ])
    def pay_table_factor(self, r):
        serializer = TableFactorSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        table = serializer.validated_data["table"]
        pay = serializer.validated_data["pay"]
        if pay:
            try:
                factor = Pay.objects.filter(table=table, success=False)
            except:
                raise ValidationError(f'Cant get obj with the given table: ({table})')
            if len(factor) > 1:
                raise ValidationError('There is more than one active factor for this table')
            elif len(factor) < 1:
                raise ValidationError('There is no active factor for this table')
            try:
                factor[0].success = True
                factor[0].save()
            except:
                raise ValidationError('Cant change success field to true.')
        else:
            raise ValidationError('Selecting the pay field is required')
        return Response('done', status=200)


class MaterialViewSet(viewsets.ModelViewSet):

    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateProductSerializer
        return ProductSerializer

    def get_serializer_context(self):
        if self.action == 'material_details':
            pass
