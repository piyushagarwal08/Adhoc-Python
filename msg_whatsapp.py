#03ad6c6d24576883f568529957f2f392        Auth
#SK3f9fb28ea5b0e1dba326c0cf85f9602a       SID
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC96e12a0bce077abf0936861bca6e8fc4'
auth_token = '03ad6c6d24576883f568529957f2f392'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+16693337498',
                     to='+919057529646'
                 )

print(message.sid)
