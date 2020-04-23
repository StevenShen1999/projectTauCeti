import os
#basedir = os.path.abspath(os.path.dirname(__file__))

class Configuration(object):
    TAUCETI_SECRET_KEY = os.environ.get('TAUCETI_SECRET_KEY')
    FLASK_DEBUG = True

    # Database
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = f"postgresql://postgres:{os.environ.get('SQLPassword')}@localhost/tauCetiDB"

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = "shenthemaster@gmail.com" #FIXME: Change this to our helper email
    MAIL_PASSWORD = "990928ss" #FIXME: os.environ.get("TAUCETI_EMAIL_PASSWORD")

