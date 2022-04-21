from rest_framework import serializers

from apps.mailings import models


class MailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mailing
        fields = (
            'id',
            'date_start',
            'date_end',
            'time_start',
            'time_end',
            'text',
            'tag',
            'mobile_operator_code',
        )
