from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab
from celery.utils.log import get_task_logger
from django.conf import settings
from sms.smsFetching import SMS


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'helplineApp.settings')
app = Celery('helplineApp')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

logger = get_task_logger(__name__)

s = SMS()

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    
    sender.add_periodic_task(10.0, receiving.s(), name='receiving sms')


@app.task
def receiving():
    
    from reports.models import Report
    import africastalking
    
    username = os.environ.get('AFRICAS_TALKING_USERNAME')
    api_key = os.environ.get('AFRICAS_TALKING_API_KEY')
    africastalking.initialize(username, api_key)
    sms = africastalking.SMS


    def fetch_sms_sync(self):

        try:
            last_received_id = os.environ.get('LAST_RECEIVED')
            while True:
                MessageData = self.sms.fetch_messages(last_received_id)
                messages = MessageData['SMSMessageData']['Messages']
                if len(messages) == 0:
                    logger.info("No sms messages in your inbox.")
                    break
                for message in messages:
                    Report.objects.create(
                                info = message['text'],
                                report_date = message['date'],
                                case_opened = 'no')
                    last_received_id = int(message['id'])
            os.environ['LAST_RECEIVED'] = last_received_id
        except Exception as e:
            print ('Encountered an error while fetching: %s' % str(e))
    logger.info("receiving sms")
    s.fetch_sms_sync()



# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))