import datetime
import os

import pytz
import requests
from celery.utils.log import get_task_logger

from apps.customers.models import Customer
from apps.mailings.models import Mailing
from notification_service.celery import app

logger = get_task_logger(__name__)

URL = os.environ.get("URL")
TOKEN = os.environ.get("TOKEN")


@app.task()
def send_message(data, client_id, mailing_id):
    mail = Mailing.objects.get(pk=mailing_id)
    client = Customer.objects.get(pk=client_id)
    timezone = pytz.timezone(client.timezone)
    now = datetime.datetime.now(timezone)

    if mail.time_start <= now.time() <= mail.time_end:
        header = {
            'Authorization': f'Bearer {TOKEN}',
            'Content-Type': 'application/json'}
        responce = requests.post(url=URL + str(data['id']), headers=header, json=data)
        return {'status': responce.status_code}
