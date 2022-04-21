from rest_framework import serializers

from apps.customers import models


class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = (
            'id',
            'phone_number',
            'mobile_operator_code',
            'timezone',
            'tag',
        )
