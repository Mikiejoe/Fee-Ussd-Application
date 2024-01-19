# works with both python 2 and 3
from __future__ import print_function

import africastalking

class SMS:
    def __init__(self):
        self.username = "sandbox"
        self.api_key = "63844ecae6efdf704ed70d2240b823184d6c48419258a10fcda65ab2847718ab"

        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        # Get the SMS service
        self.sms = africastalking.SMS

    def send(self,phone:str,balance:float):
        # Set the numbers you want to send to in international format
        recipients = [phone]

        # Set your message
        message = f"hello your balance is ${balance}";

        # Set your shortCode or senderId
        sender = "Fee-wiz"
        try:
            # Thats it, hit send and we'll take care of the rest.
            response = self.sms.send(message, recipients, sender)
            print (response)
        except Exception as e:
            print ('Encountered an error while sending: %s' % str(e))

if __name__ == '__main__':
    SMS().send()