from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from apps.customers.models import Customer
from apps.mailings.models import Mailing
from utils.tasks import send_message


class Message(models.Model):
    SENT = "sent"
    NO_SENT = "no sent"

    STATUS_CHOICES = (
        (SENT, "Sent"),
        (NO_SENT, "No sent"),
    )

    time_create = models.DateTimeField(
        verbose_name='Time create',
        auto_now_add=True,
    )
    sending_status = models.CharField(
        max_length=15,
        verbose_name='Sending status',
        choices=STATUS_CHOICES,
    )
    mailing = models.ForeignKey(
        Mailing,
        on_delete=models.CASCADE,
        related_name='message',
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='message',
    )

    def __str__(self):
        return f'Message {self.id} with text {self.mailing} for {self.customer.phone_number}'

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        ordering = ('-id',)


@receiver(post_save, sender=Mailing)
def create_message(sender, instance, created, **kwargs):
    if created:
        customers = Customer.objects.filter(
            Q(mobile_operator_code=instance.mobile_operator_code)
            | Q(tag__icontains=instance.tag)
        )

        for customer in customers:
            Message.objects.create(
                sending_status="No sent",
                customer_id=customer.id,
                mailing_id=instance.id
            )
            message = Message.objects.filter(
                mailing_id=instance.id,
                customer_id=customer.id).first()
            data = {
                'id': message.id,
                "phone": customer.phone_number,
                "text": instance.text
            }
            now = timezone.now()
            if instance.date_start <= now <= instance.date_end:
                send_message.delay(data, customer.id, instance.id)
            else:
                send_message.delay(data, customer.id, instance.id)
