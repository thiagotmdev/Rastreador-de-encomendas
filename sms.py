from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
def sms(data1, data2, cod_r):
    account_sid = 'SUA_SID'
    auth_token = 'SEU_TOKEN'
    client = Client(account_sid, auth_token)

    client.messages.create(
        body="Código rastreio: "+cod_r+" "+data1,
        from_='SEU_NUMERO_DO_TEL_TWILIO',
        to=data2
    )
