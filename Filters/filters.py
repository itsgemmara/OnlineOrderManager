from django.core.exceptions import ValidationError

from .utils import pk_response_creator, serializer_field_creator
from .serializers import *

#
# def char_field_filter()


class BaseModelFilter:

    def __init__(self, model, fields=None):
        self.model = model
        self.fields = fields

    def get_fields(self):
        fields = self.model._meta.get_fields()
        model_fields = dict()
        for field in fields:
            model_fields[field.name] = type(field)
        return model_fields

    def char_field(self):
        serializer = TextSearchFilterSerializer
        serializer_fields = ['search_key']
        filtering = 0
        return {'serializer': serializer, 'serializer_fields': serializer_fields}

    def text_field(self):
        serializer = TextSearchFilterSerializer
        serializer_fields = ['search_key']
        return {'serializer': serializer, 'serializer_fields': serializer_fields}




class BaseFilter:

    def __init__(self, data, model, serializer_fields=None, serializer=None):
        self.data = data
        self.model = model
        self.serializer_fields = serializer_fields
        self.serializer = serializer

    def create_serializer_fields(self):
        parameters = serializer_field_creator(self.serializer, self.data, self.serializer_fields)
        return parameters


class NameFilter(BaseFilter):

    def name_search_filter(self):
        self.serializer = TextSearchFilterSerializer
        self.serializer_fields = ['search_key']
        if self.serializer != TextSearchFilterSerializer:
            serializer = self.serializer(data=self.data)
            serializer.is_valid(raise_exception=True)
            try:
                serializer.validated_data['search_key']
            except Exception as e:
                raise ValidationError(f'{self.serializer} should have search_key field, '
                                      f'witch used as a search key in {self.model} instances name.')
        parameters = self.create_serializer_fields()
        filtering = self.model.objects.filter(name__contains=parameters['search_key'])
        return pk_response_creator(filtering)


def description_search_filter(data, model, serializer_fields=['search_key'], serializer=TextSearchFilterSerializer):
    parameters = serializer_field_creator(serializer, data, serializer_fields)
    filtering = model.objects.filter(description__contains=parameters['search_key'])
    return pk_response_creator(filtering)


def amount_search_filter(data, model, serializer_fields=['maximum', 'minimum'], serializer=AmountFilterSerializer):
    parameters = serializer_field_creator(serializer, data, serializer_fields)
    if parameters['maximum']:
        filtering = model.objects.filter(amount__gte=int(parameters['minimum']), amount__lte=int(parameters['maximum']))
    else:
        filtering = model.objects.filter(amount__gte=int(parameters['minimum']))
    return pk_response_creator(filtering)


def date_search_filter(data, model):
    parameters = serializer_field_creator(DateFilterSerializer, data, ['from_date', 'to_date'])
    minimum_date = parameters['from_date']
    maximum_date = parameters['to_date']
    if maximum_date and minimum_date:
        filtering = model.objects.filter(date__gte=minimum_date, date__lte=maximum_date)
    elif minimum_date:
        filtering = model.objects.filter(date__gte=minimum_date)
    elif maximum_date:
        filtering = model.objects.filter(date__lte=maximum_date)
    else:
        filtering = model.objects.all()
    return pk_response_creator(filtering)
