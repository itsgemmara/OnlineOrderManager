from rest_framework.response import Response

from rest_framework import generics, mixins, views
from rest_framework.decorators import action
from rest_framework import viewsets

from .serializers import *
from .models import Person


class PersonnelViewSet(viewsets.ModelViewSet):

    """
    General ViewSet description

    list: List personnel

    retrieve: Retrieve personnel

    update: Update personnel

    create: Create personnel

    partial_update: Patch personnel

    """

    queryset = Person.objects.all()
    serializer_class = PersonnelSerializer

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            return CreatePersonSerializer
        return PersonnelSerializer

