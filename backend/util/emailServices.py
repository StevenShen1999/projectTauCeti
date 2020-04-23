from app import app
from flask_mail import Mail

mail = Mail(app)

def sendActivationEmail(stringToSend, emailToSend):
    message = f"""\
Hello,\nIt's good to have you with us. Thanks again for signing up with tauCeti.\n\nPlease activate your account now: {stringToSend}"""

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