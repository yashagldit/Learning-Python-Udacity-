from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC6a8c0fb983bad3b144e3eed8c9185cac"
# Your Auth Token from twilio.com/console
auth_token  = "21c0d45e8ce414dd069a060192095a79"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+918004980177", 
    from_="+18562494816",
    body="Hello from Yash Agarwal!")

print(message.sid)
