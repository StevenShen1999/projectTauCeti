from app import app
from flask_mail import Mail

mail = Mail(app)

def sendActivationEmail(stringToSend, emailToSend):
    message = f"""\
Hello,\nIt's good to have you with us. Thanks again for signing up with tauCeti.\n\nPlease activate your account now: {stringToSend}\n\nIf you didn't request this, please disregard this email."""

    try:
        msg = mail.send_message(
            'Activate Your tauCeti Account',
            sender=app.config['MAIL_USERNAME'],
            recipients=[emailToSend],
            body=message
        )
    except Exception:
        return str(Exception)
    return "success"

def sendVerificationEmail(stringToSend, emailToSend):
    message = f"""\
Hey,\nIt's been a while since we've seen you.\n\nHere's your verification code: {stringToSend}.\n\nIf you didn't request this, please disregard this email."""

    try:
        msg = mail.send_message(
            'Verify Your tauCeti Account',
            sender=app.config['MAIL_USERNAME'],
            recipients=[emailToSend],
            body=message
        )
    except Exception:
        return str(Exception)
    return "success"

# Type is ['course', 'note', more to be added]
# Payload requires format:
# "oldType: 'oldValue'\nnewType: 'newValue'"
def sendRequestEmail(type, identification, payload, sender, typeName):
    type = type.upper()
    message = f"""\
Hey, \nA new request was filed by {sender} to modify:
{type} (id: {identification}, name: {typeName})

with the following changes:

{payload}"""

    try:
        msg = mail.send_message(
            f'TauCeti: Request to update {type} : {identification}',
            sender=app.config['MAIL_USERNAME'],
            recipients=["stevenshen1999@hotmail.com"], # FIXME: Change this to a collection of admin accounts
            body=message
        )
    except Exception:
        return str(Exception)
    return "success"