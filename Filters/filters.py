# from django.db.models.fields import CharField
from django.core.exceptions import ValidationError

from .utils import pk_response_creator, serializer_field_creator
from .serializers import *


class BaseFilter:

    def __init__(self, data, model, field_name=None, filter_dict=None, serializer_fields=None, serializer=None):
        self.data = data
        self.model = model
        self.serializer_fields = serializer_fields
        self.serializer = serializer
        self.field_name = field_name
        self.filter_dict = filter_dict

    def create_serializer_fields(self):
        parameters = serializer_field_creator(self.serializer, self.data, self.serializer_fields)
        return parameters

    def filter(self, filter_dict):
        filtering = self.model.objects.filter(**filter_dict)
        return pk_response_creator(filtering)

    def create_parameters(self):
        return serializer_field_creator(self.serializer, self.data, self.serializer_fields)


class Filter(BaseFilter):

    def char_field(self):
        self.serializer = TextSearchFilterSerializer
        self.serializer_fields = ['search_key']
        parameters = serializer_field_creator(self.serializer, self.data, self.serializer_fields)
        self.filter_dict = {self.field_name + '__contains': parameters['search_key']}
        return self.filter(self.filter_dict)

    def integer_field_filter(self):
        self.serializer = AmountFilterSerializer
        self.serializer_fields = ['maximum', 'minimum']
        parameters = serializer_field_creator(self.serializer, self.data, self.serializer_fields)
        if parameters['maximum']:
            self.filter_dict = {self.field_name + '__gte': int(parameters['minimum']),
                                self.field_name + '__lte': int(parameters['maximum'])}
        else:
            self.filter_dict = {self.field_name + '__gte': int(parameters['minimum'])}
        filtering = self.model.objects.filter(**self.filter_dict)
        return pk_response_creator(filtering)

    def interval_date_field_filter(self):
        self.serializer = IntervalDateFilterSerializer
        self.serializer_fields = ['from_date', 'to_date']
        parameters = serializer_field_creator(self.serializer, self.data, self.serializer_fields)
        minimum_date = parameters['from_date']
        maximum_date = parameters['to_date']
        code = None
        if maximum_date and minimum_date:
            self.filter_dict = {self.field_name + '__gte': minimum_date, self.field_name + '__lte': maximum_date}
        elif minimum_date:
            self.filter_dict = {self.field_name + '__gte': minimum_date}
        elif maximum_date:
            self.filter_dict = {self.field_name + '__lte': maximum_date}
        else:
            code = 'all'
        if code:
            filtering = self.model.objects.all()
        else:
            filtering = self.model.objects.filter(**self.filter_dict)
        return pk_response_creator(filtering)

    def date_field_filter(self):
        self.serializer = DateFilterSerializer
        self.serializer_fields = ['date']
        parameters = serializer_field_creator(self.serializer, self.data, self.serializer_fields)
        date = parameters['date']
        self.filter_dict = {self.field_name + '__contains': date}
        filtering = self.model.objects.filter(**self.filter_dict)
        return pk_response_creator(filtering)

    def choice_field(self, serializer, serializer_fields):
        self.serializer = serializer
        self.serializer_fields = serializer_fields
        parameters = serializer_field_creator(self.serializer, self.data, self.serializer_fields)
        if len(parameters) > 1:
            raise ValidationError(f'{serializer} should have just one field.')
        print(type(parameters))
        self.filter_dict = {self.field_name + '__contains': parameters[serializer_fields[0]]}
        if parameters[serializer_fields[0]] == 'all':
            filtering = self.model.objects.all()
            return pk_response_creator(filtering)
        else:
            return self.filter(self.filter_dict)

    def bool_field(self):
        self.serializer = BooleanFilterSerializer
        self.serializer_fields = ['filter_by']
        parameters = serializer_field_creator(self.serializer, self.data, self.serializer_fields)
        filter_by = parameters['filter_by']
        if filter_by == 'all':
            filtering = self.model.objects.all()
            return pk_response_creator(filtering)
        else:
            self.filter_dict = {self.field_name: parameters['filter_by']}
            return self.filter(self.filter_dict)


# class BaseModelFilter:
#
#     def __init__(self, model, fields=None):
#         self.model = model
#         self.fields = fields
#
#     def get_fields(self):
#         fields = self.model._meta.get_fields()
#         model_fields = dict()
#         field_list = list()
#         for field in fields:
#             for f in self.fields:
#                 if field.name == f:
#                     field_list.append(field)
#         for field in field_list:
#             model_fields[field.name] = type(field)
#         return model_fields
#
#     def filter(self):
#         fields = self.get_fields()
#         for field in fields:
#             if fields[field] == type(CharField):