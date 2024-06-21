import pika
import django
import os
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

import pika.connection

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'listingservice.settings')
django.setup()

from quickstart.models import Listing

def callback(ch, method, properties, body):
    message = body.decode()
    company_id = message.split()[-2]
    
    try:
        listing = Listing.objects.get(companyid=company_id)
        listing.delete()
        print('Deleted listing related to company with ID:', company_id)
    except ObjectDoesNotExist:
        print('No listing found related to company with ID:', company_id)
    except MultipleObjectsReturned:
        listings = Listing.objects.filter(companyid=company_id)
        for listing in listings:
            listing.delete()
        print('Deleted multiple listings related to company with ID:', company_id)
    
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit'))
channel = connection.channel()

channel.queue_declare(queue='company_deletion_queue')
channel.basic_consume(queue='company_deletion_queue', on_message_callback=callback, auto_ack=True)

channel.start_consuming()