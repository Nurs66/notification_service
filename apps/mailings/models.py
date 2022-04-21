from django.db import models


class Mailing(models.Model):
    date_start = models.DateTimeField(
        verbose_name='Mailing start'
    )
    date_end = models.DateTimeField(
        verbose_name='End of mailing'
    )
    time_start = models.TimeField(
        verbose_name='Start time to send message'
    )
    time_end = models.TimeField(
        verbose_name='End time to send message'
    )
    text = models.TextField(
        verbose_name='Message text'
    )
    tag = models.CharField(
        max_length=100,
        verbose_name='Search by tags',
    )
    mobile_operator_code = models.CharField(
        max_length=5,
        verbose_name='Search by mobile operator code',
    )

    class Meta:
        verbose_name = 'Mailing'
        verbose_name_plural = 'Mailings'
        ordering = ('-id',)
