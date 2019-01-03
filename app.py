from twilio.rest import TwilioRestClient
from credentials import account_sid, auth_token, my_tel, my_twil

client = TwilioRestClient(account_sid, auth_token)

my_message = "Helllo From My App"

message = client.messages.create(to=my_tel, from_= my_twil, body=my_message)

print ('Message sent')