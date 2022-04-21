from rest_framework import serializers

from apps.customers.serializers import ConsumerSerializer
from apps.mailings.serializers import MailingSerializer
from apps.message import models


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Message
        fields = (
            'id',
            'time_create',
            'sending_status',
            'mailing',
            'customer',
        )


class MessagesDetailSerializer(serializers.ModelSerializer):
    mailing = MailingSerializer(read_only=True)
    customer = ConsumerSerializer(read_only=True)

    class Meta:
        model = models.Message
        fields = (
            'id',
            'time_create',
            'sending_status',
            'mailing',
            'customer',
        )
