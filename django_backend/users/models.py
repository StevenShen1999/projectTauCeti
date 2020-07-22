from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ExtendedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    activated = models.BooleanField(default=True)
    points = models.FloatField(default=0)
    # Link is the referral link issued by this user, not yet implemeneted
    link = models.CharField(max_length=255)
    role = models.IntegerField()
    verification_code = models.CharField(max_length=255)
    failed_logins = models.IntegerField()
    locked_until = models.DateTimeField()
    profile_image = models.CharField(max_length=255)

    # TODO: Foreign Keys go here

    def __str__(self):
        return f"{self.email}, {self.username}"