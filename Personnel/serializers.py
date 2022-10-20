from rest_framework import serializers

from .models import Person
from .utils import category_choices_creator


class PersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class CreatePersonSerializer(serializers.ModelSerializer):

    CAT = list(category_choices_creator())
    CAT.append(('something_else', 'Something else'))
    CAT.append(('all', 'All'))
    duties = serializers.MultipleChoiceField(choices=tuple(CAT))

    class Meta:
        model = Person
        fields = ('name', 'last_name', 'duties', 'description')
