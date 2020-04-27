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
            'Activate Your tauCeti Account',
            sender=app.config['MAIL_USERNAME'],
            recipients=[emailToSend],
            body=message
        )
    except Exception:
        return str(Exception)
    return "success"