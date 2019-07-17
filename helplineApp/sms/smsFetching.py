from __future__ import print_function
from __future__ import absolute_import, unicode_literals
import os
import africastalking


class SMS():
    def __init__(self):
        self.username = os.environ.get('AFRICAS_TALKING_USERNAME')
        self.api_key = os.environ.get('AFRICAS_TALKING_API_KEY')
        africastalking.initialize(self.username, self.api_key)
        self.sms = africastalking.SMS


    def fetch_sms_sync(self):
        try:
            last_received_id = os.environ.get('LAST_RECEIVED')
            while True:
                MessageData = self.sms.fetch_messages(last_received_id)
                messages = MessageData['SMSMessageData']['Messages']
                if len(messages) == 0:
                    print ('No sms messages in your inbox.')
                    break
                for message in messages:
                    print (message)
                    # self.create_report(message['text'],message['date'],'no')
                    last_received_id = int(message['id'])
            os.environ['LAST_RECEIVED'] = last_received_id
        except Exception as e:
            print ('Encountered an error while fetching: %s' % str(e))

if __name__ == '__main__':
    SMS().fetch_sms_sync()

