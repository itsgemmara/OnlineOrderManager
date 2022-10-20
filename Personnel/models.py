from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    duties = models.CharField(max_length=1000)
    date_joined = models.DateTimeField(auto_now=True)
    description = models.TextField(null=True, blank=True)


