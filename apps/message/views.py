from rest_framework import viewsets

from apps.message import models
from apps.message import serializers


class MessageViewSet(viewsets.ModelViewSet):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessagesSerializer

    def get_serializer_class(self):
        if self.action in ['retrieve']:
            return serializers.MessagesDetailSerializer
        return self.serializer_class
