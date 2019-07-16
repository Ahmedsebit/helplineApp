from __future__ import print_function

import africastalking

class SMS:
    def __init__(self):
        self.username = "set_the_user_name_here"
        self.api_key = "set_the_api_key_here"

        africastalking.initialize(self.username, self.api_key)

        self.sms = africastalking.SMS

    def fetch_sms_sync(self):
        try:
            last_received_id = 0
            while True:
                MessageData = self.sms.fetch_messages(last_received_id)
                messages = MessageData['SMSMessageData']['Messages']
                if len(messages) == 0:
                    print ('No sms messages in your inbox.')
                    break
                for message in messages:
                    print (message)
                    last_received_id = int(message['id'])

        except Exception as e:
            print ('Encountered an error while fetching: %s' % str(e))

if __name__ == '__main__':
    SMS().fetch_sms_sync()