# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACb5006b36ad6a2ada649fc4f56cacd1fc'
auth_token = 'dc98ffcd5fc4e2f5f7278c7cf6d00644'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+13343264809',
                     to='+254729174754'
                 )

print(message.sid)

