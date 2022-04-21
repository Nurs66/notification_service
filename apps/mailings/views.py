from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.mailings import models
from apps.mailings import serializers
from apps.message.models import Message
from apps.message.serializers import MessagesSerializer


class MailingViewSet(viewsets.ModelViewSet):
    queryset = models.Mailing.objects.all()
    serializer_class = serializers.MailingSerializer

    @action(detail=True, methods=['get'])
    def detail_view(self, request, pk=None):
        queryset_mailing = models.Mailing.objects.all()
        get_object_or_404(queryset_mailing, pk=pk)
        queryset = Message.objects.filter(mailing_id=pk).all()
        serializer = MessagesSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def statistic(self, request, pk=None):
        total_count = models.Mailing.objects.count()
        mailing = models.Mailing.objects.values('id')
        content = {'Total of mailings': total_count,
                   'Message sent': ''}
        result = {}

        for row in mailing:
            total_result = {'Total message': 0, 'Sent': 0, 'No sent': 0}
            mail = Message.objects.filter(mailing_id=row['id']).all()
            group_sent = mail.filter(sending_status='sent').count()
            group_no_sent = mail.filter(sending_status='no sent').count()
            total_result['Total message'] = len(mail)
            total_result['Sent'] = group_sent
            total_result['No sent'] = group_no_sent
            result[row['id']] = total_result

        content['Message sent'] = result
        return Response(content)
