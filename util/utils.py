from random import randint
from twilio.rest import Client


def random_with_N_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


def sendConfirmSMS(phone, text, token):
    account_sid = 'AC4e28898dd0e4576fd778f8b3f9e09e46'
    auth_token = 'dbe8e5ef217134d66df49e2ec6c53200'
    client = Client(account_sid, auth_token)

    client.messages \
        .create(
        body=text + token,
        from_='+12076002473',
        to=phone
    )
    return True
