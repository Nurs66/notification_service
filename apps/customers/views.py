from rest_framework import viewsets

from apps.customers import models
from apps.customers import serializers


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.ConsumerSerializer
