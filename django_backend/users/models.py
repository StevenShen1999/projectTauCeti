from django.db import models

# Create your models here.
class Users(models.Model):
    email = models.CharField(null=False, db_index=True)
    username = models.CharField(max_length=255)
    password = models.CharField()
    activated = models.BooleanField(default=True)
    points = models.FloatField(default=0)
    # Link is the referral link issued by this user, not yet implemeneted
    link = models.CharField()
    created_date = models.DateTimeField(auto_now_add=True)
    role = models.IntegerField()
    last_login = models.DateTimeField()
    verification_code = models.CharField()
    failed_logins = models.IntegerField()
    locked_until = models.DateTimeField()
    profile_image = models.CharField()

    # TODO: Foreign Keys go here