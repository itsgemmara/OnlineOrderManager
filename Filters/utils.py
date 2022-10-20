from django.core.exceptions import ValidationError


def pk_response_creator(filtering):
    response = list()
    for i in filtering:
        response.append(i.pk)
    return response


def serializer_field_creator(serializer, data, serializer_fields):
    serializer = serializer(data=data)
    serializer.is_valid(raise_exception=True)
    if type(serializer_fields) != list:
        raise ValidationError(f'serializer_fields should be a list of fields. not {type(serializer_fields)}')
    response = dict()
    for field in serializer_fields:
        response[field] = serializer.validated_data[field]
    return response


def period_choices_creator():
    PERIOD = (('day', 'هر روز'),
              ('week', 'هر هفته'),
              ('month', 'هر ماه'),
              ('three_month', 'هر سه ماه'),
              ('six_month', 'هر شش ماه'),
              ('year', 'هر سال'),)
    return PERIOD
